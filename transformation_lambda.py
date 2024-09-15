import json
import base64
from datetime import datetime

def lambda_handler(event, context):
    output = []
    
    for record in event['Records']:
        try:
            raw_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
            print(f"Raw data: {raw_data}")  # Add logging
            
            data = json.loads(raw_data) 
            
            #Transformation: Add processed timestamp
            data['processed_timestamp'] = datetime.utcnow().isoformat()
        
            #Transformation: Rename columns
            if 'HR' in data:
                data['heart_rate'] = data.pop('HR')
            if 'NBP Sys' in data:
                data['systolic_bp'] = data.pop('NBP Sys')
            if 'NBP Dia' in data:
                data['diastolic_bp'] = data.pop('NBP Dia')
            if 'NBP Mean' in data:
                data['mean_bp'] = data.pop('NBP Mean')
            if 'awRR' in data:
                data['respiratory_rate'] = data.pop('awRR')
            if 'Temperature' in data:
                data['temperature'] = data.pop('Temperature')
            if 'AWP' in data:
                data['AwP'] = data.pop('AWP')
            if 'Pulse' in data:
                data['pulse'] = data.pop('Pulse')
        
            #Transformation: Ensure correct data types
            data['heart_rate'] = int(data['heart_rate'])
            data['systolic_bp'] = int(data['systolic_bp'])
            data['diastolic_bp'] = int(data['diastolic_bp'])
            data['mean_bp'] = int(data['mean_bp'])
            data['pulse'] = int(data['pulse'])
            data['SpO2'] = int(data['SpO2'])
            data['respiratory_rate'] = int(data['respiratory_rate'])
            data['temperature'] = round(float(data['temperature']))
            data['etSEV'] = round(float(data['etSEV']))
            data['inSEV'] = round(float(data['inSEV']))
            data['etDES'] = round(float(data['etDES']))
            data['inDES'] = round(float(data['inDES']))
            data['etISO'] = round(float(data['etISO']))
            data['inISO'] = round(float(data['inISO']))
            data['etN2O'] = round(float(data['etN2O']))
            data['inN2O'] = round(float(data['inN2O']))
            data['MAC'] = round(float(data['MAC']))
        
            #Re-encode the transformed data
            output_record = {
                'result': 'Ok',
                'data': base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8')
            }
            output.append(output_record)
        
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Error Processing record: {e}")
            output_record = {
                'result': 'ProcessingFailed',
                'data': record['kinesis']['data']
            }
            output.append(output_record)

    return{'Records': output}