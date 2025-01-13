import random
import json
from datetime import datetime
import os
from dotenv import load_dotenv
from paho.mqtt import client as mqtt_client
from azure.iot.device import IoTHubDeviceClient, Message
import pytz
import logging

load_dotenv()

# logging.basicConfig(level=logging.DEBUG)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

# Paho MQTT connection details
broker = 'mosquitto'
port = 1883
topics = ["zigbee2mqtt/test_device_1", "zigbee2mqtt/test_device_2"]  # List of topics
client_id = f'python-mqtt-{random.randint(0, 100)}'
singapore = pytz.timezone('Asia/Singapore')


# IoT Hub connection string
# IOT_HUB_CONNECTION_STRING = 'HostName=CPF-IOT-HUB.azure-devices.net;DeviceId=Device-2;SharedAccessKey=Ek5i4e0Uq0n8AB1EAssOfcEJXqwC6xPRiPOMJxRV4JA='
IOT_HUB_CONNECTION_STRING = 'HostName=CPF-IOT-HUB.azure-devices.net;DeviceId=device-1;SharedAccessKey=QsuvFYqsfJdH+3/cWbSI2Im1bTNSr9mCSI9Mi+qu+Nw='


# Dictionary to store the last known "presence" status of each device
last_presence_status = {}

# Dictionary to store the last time a "presence" message was sent for each device
last_sent_time = {}

# Time threshold in seconds (5 minutes)
TIME_THRESHOLD = 5 * 60

def connect_mqtt() -> mqtt_client.Client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}\n")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client.Client):
    def on_message(client, userdata, msg):
        logging.debug(f"MQTT message received: {msg.topic} {msg.payload.decode('utf-8')}")

        try:
            # Decode the original message payload
            decoded_payload = msg.payload.decode('utf-8')
            message_dict = json.loads(decoded_payload)

            # Extract the device name from the topic
            device_name = msg.topic.split('/')[-1]

            # Check if "presence" field exists in the message
            if "presence" in message_dict:
                current_presence = message_dict["presence"]
                current_time = datetime.now(pytz.utc).astimezone(singapore)

                # Compare the current "presence" with the last known "presence"
                if device_name in last_presence_status:
                    if current_presence == last_presence_status[device_name]:
                        # Check if the timer has exceeded the threshold
                        if device_name in last_sent_time:
                            elapsed_time = (current_time - last_sent_time[device_name]).total_seconds()
                            if elapsed_time > TIME_THRESHOLD:
                                logging.info(f"Timer exceeded for {device_name}. Resending 'presence' message.")
                                # Add the current Singapore time to the message
                                message_dict['timestamp'] = current_time.isoformat()
                                message_dict['device_name'] = device_name

                                # Convert the updated dictionary back to a JSON string
                                updated_payload = json.dumps(message_dict)

                                # Create a message and send it to IoT Hub
                                iot_message = Message(updated_payload)
                                iot_message.content_encoding = "utf-8"
                                iot_message.content_type = "application/json"
                                iothub_client.send_message(iot_message)
                                logging.info(f"Message resent to IoT Hub: {updated_payload}")

                                # Update the last sent time
                                last_sent_time[device_name] = current_time

                        logging.debug(f"No significant change in 'presence' status for {device_name}. Skipping message.")
                        return  # Skip sending the message since there's no change

                # Update the last known "presence" status and reset the timer
                last_presence_status[device_name] = current_presence
                last_sent_time[device_name] = current_time

            # Add the current Singapore time to the message
            current_singapore_time = current_time.isoformat()
            message_dict['timestamp'] = current_singapore_time
            message_dict['device_name'] = device_name

            # Convert the updated dictionary back to a JSON string
            updated_payload = json.dumps(message_dict)

            # Create a message and send it to IoT Hub
            iot_message = Message(updated_payload)
            iot_message.content_encoding = "utf-8"
            iot_message.content_type = "application/json"
            iothub_client.send_message(iot_message)
            logging.info(f"Message sent to IoT Hub: {updated_payload}")

        except Exception as e:
            logging.error(f"Failed to send message to IoT Hub: {e}")

    # Subscribe to each topic in the list
    for t in topics:
        client.subscribe(t)
        print(f"Subscribed to topic: {t}")

    client.on_message = on_message

iothub_client = IoTHubDeviceClient.create_from_connection_string(IOT_HUB_CONNECTION_STRING)

def run():

    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
