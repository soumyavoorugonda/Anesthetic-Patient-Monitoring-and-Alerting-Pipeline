import json
import boto3
import base64

# Initialize the SNS client
sns_client = boto3.client('sns')
sns_topic_arn = 'sns_arn'


def check_heart_rate(HR):
    if HR < 50:
        return f"Heart Rate too low: {HR} bpm"
    elif HR > 150:
        return f"Heart Rate too high: {HR} bpm"
    return None

def check_spo2(SpO2):
    if SpO2 < 90:
        return f"Low Oxygen Saturation: SpO2 {SpO2}% (Hypoxemia)"
    return None

def check_etco2(etCO2):
    if etCO2 < 30:
        return f"End-Tidal CO2 too low: {etCO2} mmHg (Hypocapnia)"
    elif etCO2 > 50:
        return f"End-Tidal CO2 too high {etCO2} mmHg (Hypercapnia)"
    return None

def check_respiratory_rate(awRR):
    if awRR < 12:
        return f"Low Respiratory Rate {awRR} breaths per minute"
    elif awRR > 20:
        return f"High Respiratory Rate {awRR} breaths per minute"
    return None

def check_temperature(Temperature):
    Temperature = float(Temperature)
    Temperature = round(Temperature, 1)
    if Temperature < 36.1:
        return f"Temperature is too low {Temperature}°C"
    elif Temperature > 37.8:
        return f"Temperature is too high {Temperature}°C"
    return None


def lambda_handler(event, context):
    try:
        patient_id = "Patient 1"
        for record in event['Records']:
            payload = json.loads(base64.b64decode(record['kinesis']['data']).decode('utf-8'))  # Directly parsing JSON data

            alerts = []
            
            # Individual metric checks
            alerts.append(check_heart_rate(payload.get('HR')))
            alerts.append(check_spo2(payload.get('SpO2')))
            alerts.append(check_etco2(payload.get('etCO2')))
            alerts.append(check_respiratory_rate(payload.get('awRR')))
            alerts.append(check_temperature(payload.get('Temperature')))

            # Filter out None values from alerts
            alerts = list(filter(None, alerts))

            # If any alerts are triggered, send them to SNS
            if alerts:
                alert_message = f"Alert for {patient_id}: " + " | ".join(alerts)
                sns_response = sns_client.publish(
                    TopicArn=sns_topic_arn,
                    Message=alert_message,
                    Subject='Critical Medical Alert'
                )
                print(f"Alert sent to SNS: {sns_response}")

        return {
            'statusCode': 200,
            'body': json.dumps('Successfully processed records.')
        }
    
    except Exception as e:
        print(f"Error processing record: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing records.')
        }
