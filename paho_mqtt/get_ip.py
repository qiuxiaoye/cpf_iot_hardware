import socket
import connect_to_iot_hub
import json

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def send_ip_to_cloud():
    connect_to_iot_hub.send_message(get_ip_address())

send_ip_to_cloud()