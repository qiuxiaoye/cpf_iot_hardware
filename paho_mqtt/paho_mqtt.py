import random
import json
from datetime import datetime
from paho.mqtt import client as mqtt_client
import cosmos_container
# from ..mango.pymongo_get_database import get_database

# mongodb connection
# dbname = get_database()
# collection_name = dbname["user_1_items"]

# paho connection
broker = 'mosquitto'
port = 1883
topic = "zigbee2mqtt/home_switch"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # client = mqtt_client.Client(client_id)
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        json_msg=json.loads(str(msg.payload.decode("utf-8")))
        # y = json.dumps(msg.payload.decode())
        # json_msg['_id'] = 'aqara_motion_sensor'
        # json_msg['timestamp'] = datetime.now()
        # json_msg['device_name'] = "aqara_meeting_room"
        print(json_msg)
        # cosmos_container.insert_data(json_msg)
        cosmos_container.send_single_message(json_msg);
        
        # collection_name.insert_one(json_msg)
        # collection_name.insert_one(y)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
