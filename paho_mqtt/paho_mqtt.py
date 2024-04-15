import random
import json
from datetime import datetime
from paho.mqtt import client as mqtt_client
import cosmos_container
from azure.iot.device import IoTHubDeviceClient, Message

# from ..mango.pymongo_get_database import get_database

# mongodb connection
# dbname = get_database()
# collection_name = dbname["user_1_items"]

# paho connection
broker = 'mosquitto'
port = 1883
topic = "zigbee2mqtt/present_sensor"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'

IOT_HUB_CONNECTION_STRING = "HostName=CPF-IOT-HUB.azure-devices.net;DeviceId=device-1;SharedAccessKey=QsuvFYqsfJdH+3/cWbSI2Im1bTNSr9mCSI9Mi+qu+Nw="

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        # json_msg=json.loads(str(msg.payload.decode("utf-8")))
        # # y = json.dumps(msg.payload.decode())
        # # json_msg['_id'] = 'aqara_motion_sensor'
        # # json_msg['timestamp'] = datetime.now()
        # # json_msg['device_name'] = "aqara_meeting_room"
        # print(json_msg)
        # # cosmos_container.insert_data(json_msg)
        # cosmos_container.send_single_message(json_msg);
    
        print(f"MQTT message received: {msg.topic} {str(msg.payload)}")
        try:
            # Create a message and send it to IoT Hub
            iot_message = Message(msg.payload)
            iot_message.content_encoding = "utf-8"
            iot_message.content_type = "application/json"
            iothub_client.send_message(iot_message)
            print("Message successfully sent to Azure IoT Hub")
        except Exception as e:
            print(f"Failed to send message to IoT Hub: {e}")
            
            # collection_name.insert_one(json_msg)
            # collection_name.insert_one(y)

    client.subscribe(topic)
    client.on_message = on_message

iothub_client = IoTHubDeviceClient.create_from_connection_string(IOT_HUB_CONNECTION_STRING)


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
