import boto3
import json
import random
import time
from datetime import datetime, timedelta

# AWS Kinesis client initialization
kinesis_client = boto3.client('kinesis', region_name='us-east-2')
stream_name = 'AnesthesiaDashboardingStream'

# Function to generate a single patient record dynamically
def generate_patient_record(patient_id, relative_time):
    return {
        "Time": datetime.now().isoformat(),
        "RelativeTimeMilliseconds": relative_time,
        "HR": random.randint(60, 100),
        "sysNBP": random.randint(100, 140),
        "diaNBP": random.randint(60, 90),
        "meanNBP": random.randint(70, 110),
        "Pulse": random.randint(60, 100),
        "SpO2": random.randint(85, 100),
        "etCO2": random.randint(25, 52),
        "awRR": random.randint(9, 20),
        "etSEV": round(random.uniform(0.5, 2.5), 2),
        "inSEV": round(random.uniform(0.5, 2.5), 2),
        "etDES": round(random.uniform(1.0, 7.0), 2),
        "inDES": round(random.uniform(1.0, 7.0), 2),
        "etISO": round(random.uniform(0.5, 1.2), 2),
        "inISO": round(random.uniform(0.5, 1.2), 2),
        "etN2O": round(random.uniform(30.0, 75.0), 2),
        "inN2O": round(random.uniform(30.0, 70.0), 2),
        "MAC": round(random.uniform(0.5, 2.0), 2),
        "Temperature": round(random.uniform(35.0, 39.0), 1),
        "BIS": random.randint(30, 60),
        "AWP": random.randint(5, 20),
        "patient_id": f"Patient{patient_id}"
    }

# Function to send data to Kinesis
def send_to_kinesis(record):
    kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(record),
        PartitionKey=record['patient_id']
    )
    print(f"Sent record: {record}")

# Continuous streaming loop
def continuous_streaming(num_patients, interval_seconds=10, num_iterations = 100):
    start_time = datetime.now()
    relative_time = 0  # Tracks elapsed time in milliseconds

    for _ in range(num_iterations):
        for patient_id in range(1, num_patients + 1):
            # Generate and send a record for each patient
            record = generate_patient_record(patient_id, relative_time)
            send_to_kinesis(record)
        time.sleep(interval_seconds)  # Wait before generating the next set of records
        relative_time += interval_seconds * 1000  # Update relative time (in ms)

# Start continuous streaming for 3 patients with a 10-second interval
continuous_streaming(num_patients=3, interval_seconds=10, num_iterations=10)
