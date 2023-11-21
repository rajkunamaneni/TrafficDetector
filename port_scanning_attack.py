import socket
import sys

TARGET_IP = "10.0.0.46"  # Replace with the target IP address
PORT_RANGE = range(20, 1025)  # Common ports

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            print(f"Port {port} is open")
    except:
        pass

for port in PORT_RANGE:
    scan_port(TARGET_IP, port)

print("Port scan simulation completed.")
