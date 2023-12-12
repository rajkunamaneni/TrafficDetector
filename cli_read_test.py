import time
import re
import boto3
from botocore.exceptions import ClientError

# AWS SES configuration
ses_client = boto3.client('ses', region_name='us-west-1')  
sender_email = 'gmummaneni@ucdavis.edu'
recipient_email = 'mummaneni.guneet@protonmail.com'

ddos_subject = 'DDoS Attack Detected'
port_scan_subject = 'Port Scan Attack Detected'

def read_email_body(file_name):
    with open(file_name, 'r') as file:
        return file.read()

ddos_body_text = read_email_body('ddos_attack_text.txt')
port_scan_body_text = read_email_body('port_scan_attack_text.txt')

# Path to the SNORT log file
log_file_path = '/home/ubuntu/scripts/snort_output.log'

# Pattern to search for indicating a DDoS attack
ddos_pattern = re.compile(r"Possible DDoS Attack Detected")
port_scan_pattern = re.compile(r"Classification: Attempted Information Leak")

def send_email(subject, body_text):
    try:
        response = ses_client.send_email(
            Source=sender_email,
            Destination={'ToAddresses': [recipient_email]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body_text}}
            }
        )
        print("Email sent! Message ID:", response['MessageId'])
    except ClientError as e:
        print("Error sending email:", e.response['Error']['Message'])

def monitor_log_file():
    with open(log_file_path, 'r') as file:
        file.seek(0, 2)  # Go to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Wait briefly for new output
                continue
            if ddos_pattern.search(line):
                print(f"DDOS Alert: {line.strip()}")
                send_email(ddos_subject, ddos_body_text)
            elif port_scan_pattern.search(line):
                print(f"Port Scan Alert: {line.strip()}")
                send_email(port_scan_subject, port_scan_body_text)

if __name__ == "__main__":
    monitor_log_file()
