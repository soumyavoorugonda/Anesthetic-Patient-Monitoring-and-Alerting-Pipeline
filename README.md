# Anesthetic-Patient-Monitoring-and-Alerting-Pipeline
### Objective: 
The primary objective of this project is to develop a real-time anesthesia monitoring pipeline designed to enhance patient safety and support clinical decision-making during surgical procedures. The pipeline will feature a dynamic dashboard that updates every 10 seconds, providing up-to-date readings of critical vital signs such as heart rate, blood pressure, oxygen saturation, and end-tidal CO2. It will also include an alert mechanism to promptly notify medical staff of any deviations from normal ranges, ensuring immediate attention to potential emergencies.

### Dataset:
To replicate real-time data streaming for this pipeline, I employed a Python simulation script utilizing the [University of Queensland Vital Signs Dataset](https://outbox.eait.uq.edu.au/uqdliu3/uqvitalsignsdataset/index.html). This approach effectively mimics the dynamics of real-time data flow.

### Tools & Services used:
- AWS Kinesis Data Streams
- AWS Lambda
- AWS SNS
- VS Code

### Real-time Anesthesia Monitoring and Alerting Pipeline Architecture




### Alerting
The real-time patient monitoring was successfully streamed, with notifications sent to subscribers via email.


![Screenshot 2024-09-02 at 11 49 03 PM](https://github.com/user-attachments/assets/9f69f633-315f-43c6-8fb5-f4af7cde60dd)


![Screenshot 2024-09-02 at 11 52 09 PM](https://github.com/user-attachments/assets/72ebf726-9295-418e-8f12-0866759fa2f9)
