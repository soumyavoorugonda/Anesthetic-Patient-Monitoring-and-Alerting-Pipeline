import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(n, low, high):
    return np.random.randint(low, high + 1, n)

num_records = 360  # number of records for an hour at 10-second intervals
num_patients = 2

# Time settings for simulation
start_time = datetime.now()
time_series = [start_time + timedelta(seconds=10 * i) for i in range(num_records)]
relative_time_milliseconds = [i * 10000 for i in range(num_records)]  # 10000 ms per record

# Generate and save data for each patient
for patient_id in range(1, num_patients + 1):
    patient_data = pd.DataFrame({
        'Time': time_series,
        'RelativeTimeMilliseconds': relative_time_milliseconds,
        'HR': generate_data(num_records, 60, 100),
        'NBP Sys': generate_data(num_records, 100, 140),
        'NBP Dia': generate_data(num_records, 60, 90),
        'NBP Mean': generate_data(num_records, 70, 110),
        'Pulse': generate_data(num_records, 60, 100),
        'SpO2': generate_data(num_records, 85, 100),
        'etCO2': generate_data(num_records, 25, 52),
        'awRR': generate_data(num_records, 9, 20),
        'etSEV': np.random.uniform(0.5, 2.5, num_records),
        'inSEV': np.random.uniform(0.5, 2.5, num_records),
        'etDES': np.random.uniform(1.0, 7.0, num_records),
        'inDES': np.random.uniform(1.0, 7.0, num_records),
        'etISO': np.random.uniform(0.5, 1.2, num_records),
        'inISO': np.random.uniform(0.5, 1.2, num_records),
        'etN2O': np.random.uniform(30.0, 75.0, num_records),
        'inN2O': np.random.uniform(30.0, 70.0, num_records),
        'MAC': np.random.uniform(0.5, 2.0, num_records),
        'Temperature': np.random.uniform(35.0, 39.0, num_records),
        'BIS': generate_data(num_records, 30, 60),
        'AWP': generate_data(num_records, 5, 20)
    })

    # Save to CSV
    file_name = f'Patient{patient_id}_data.csv'
    patient_data.to_csv(file_name, index=False)
    print(f'Data for Patient {patient_id} saved to {file_name}')