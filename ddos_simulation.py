import requests

# Target IP Address of your Raspberry Pi
TARGET_IP = "10.0.0.46"  # Replace with the actual IP address of your Raspberry Pi
PORT = 80  # Replace with the target port, if different from 80

# Construct the URL from IP and port
TARGET_URL = f"http://{TARGET_IP}:{PORT}"

# Number of requests to send
REQUEST_COUNT = 1000

def send_request():
    for _ in range(REQUEST_COUNT):
        try:
            response = requests.get(TARGET_URL)
            print(f"Request sent to {TARGET_IP}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request to {TARGET_IP} failed: {e}")
            break  # Break the loop and stop further requests after the first failure

# Call the function directly
send_request()

print("Process completed. Stopped after encountering a connection issue.")
