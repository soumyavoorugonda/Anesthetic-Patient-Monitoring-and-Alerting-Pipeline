import boto3
import pandas as pd
import json

# Initialize a boto3 client
client = boto3.client('kinesis', region_name='us-east-2') 

# Load the CSV file
data = pd.read_csv('Patient_1_data.csv')

# Function to convert data to JSON and send to Kinesis
def send_data_to_kinesis(stream_name, data_frame):
    for index, row in data_frame.iterrows():
        # Convert the row to JSON format
        data_json = json.dumps(row.to_dict())
        
        # Send the data to Kinesis
        client.put_record(
            StreamName=stream_name,
            Data=data_json,
            PartitionKey=str(row['Time'])
        )

# Send data to Kinesis
stream_name = 'AnesthesiaMonitoringStream'
send_data_to_kinesis(stream_name, data)
