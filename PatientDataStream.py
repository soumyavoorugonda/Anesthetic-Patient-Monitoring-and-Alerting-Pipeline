import boto3
import pandas as pd
import os
import time
import json

# Initialize Kinesis client
kinesis_client = boto3.client('kinesis', region_name='us-east-2')
stream_name = 'AnesthesiaDashboardingStream'

# Function to read data from a CSV file and stream it to Kinesis
def stream_csv_to_kinesis(file_path, patient_id):
    df = pd.read_csv(file_path)
    df['patient_id'] = patient_id
    for _, row in df.iterrows():
        # Convert the row to a JSON object
        data = row.to_dict()
        # Send the data to Kinesis
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=patient_id
        )
        time.sleep(0.1)  # Adding a small delay to simulate streaming

# Directory containing the CSV files
data_directory = '/Users/soumyavoorugonda/DataScience/Projects/Anesthetic Patient Monitoring and Alerting Pipeline/Anesthetic-Patient-Monitoring-and-Alerting-Pipeline/PatientData'

# Iterate over each file in the directory and stream the data
for filename in os.listdir(data_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_directory, filename)
        if os.path.isfile(file_path):
            # Use the filename as the patient ID
            patient_id = filename.split('_')[0]
            stream_csv_to_kinesis(file_path, patient_id)
