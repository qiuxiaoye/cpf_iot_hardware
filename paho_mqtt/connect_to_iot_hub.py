from azure.iot.device import IoTHubDeviceClient, Message
import json

CONNECTION_STRING = "HostName=CPF-IOT-HUB.azure-devices.net;DeviceId=device-1;SharedAccessKey=QsuvFYqsfJdH+3/cWbSI2Im1bTNSr9mCSI9Mi+qu+Nw="

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def send_message(msg):
    client = iothub_client_init()
    msg = json.dumps(msg)
    iot_message = Message(msg)
    iot_message.content_encoding = "utf-8"
    iot_message.content_type = "application/json"
    client.send_message(iot_message)
    