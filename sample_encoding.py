import base64
import json

# Data 1
data1 = {
  "Time": "2024-09-03 15:21:17.401525",
  "RelativeTimeMilliseconds": 3580000,
  "HR": 77,
  "NBP Sys": 101,
  "NBP Dia": 69,
  "NBP Mean": 106,
  "Pulse": 81,
  "SpO2": 95,
  "etCO2": 44,
  "awRR": 15,
  "etSEV": 1.3622695671865688,
  "inSEV": 0.5842958834707992,
  "etDES": 4.56186148157573,
  "inDES": 6.148804798262254,
  "etISO": 1.1131562209954913,
  "inISO": 0.5233630880708298,
  "etN2O": 64.17910997536002,
  "inN2O": 41.91033952167423,
  "MAC": 1.5153366298309583,
  "Temperature": 36.12510163969645,
  "BIS": 44,
  "AWP": 17,
  "patient_id": "Patient1"
}

# Data 2
data2 = {
  "Time": "2024-09-03 15:21:27.401525",
  "RelativeTimeMilliseconds": 3590000,
  "HR": 81,
  "NBP Sys": 137,
  "NBP Dia": 80,
  "NBP Mean": 110,
  "Pulse": 92,
  "SpO2": 96,
  "etCO2": 27,
  "awRR": 11,
  "etSEV": 2.3879750286564576,
  "inSEV": 0.7008823294435957,
  "etDES": 2.155064768420055,
  "inDES": 3.050892427980436,
  "etISO": 0.943373477061554,
  "inISO": 1.1448930442219505,
  "etN2O": 48.90799570080934,
  "inN2O": 32.2055393564864,
  "MAC": 1.9058332180848665,
  "Temperature": 36.28499910090334,
  "BIS": 52,
  "AWP": 10,
  "patient_id": "Patient1"
}

encoded_data1 = base64.b64encode(json.dumps(data1).encode('utf-8')).decode('utf-8')
encoded_data2 = base64.b64encode(json.dumps(data2).encode('utf-8')).decode('utf-8')

print(f"Encoded Data 1: {encoded_data1}")
print(f"Encoded Data 2: {encoded_data2}")