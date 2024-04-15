import os
import json
from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message
from azure.cosmos import CosmosClient, exceptions, PartitionKey


# Load environment variables from .env file
load_dotenv()

CONNECTION_STRING = "HostName=CPF-IOT-HUB.azure-devices.net;DeviceId=device-1;SharedAccessKey=QsuvFYqsfJdH+3/cWbSI2Im1bTNSr9mCSI9Mi+qu+Nw="

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

client_iot = iothub_client_init()

# Accessing the variables
cosmos_endpoint = os.getenv('COSMOS_ENDPOINT')
cosmos_key = os.getenv('COSMOS_KEY')

client = CosmosClient(cosmos_endpoint, credential=cosmos_key)
print(client.get_database_account)

database_name = os.getenv('COSMOS_DATABASE_NAME')
container_name = os.getenv('COSMOS_CONTAINER_NAME')
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

def insert_data(data):
    # Check if data is a list and iterate over items
    if isinstance(data, list):
        for item in data:
            container.upsert_item(item)
    else:
        # If data is a single dictionary, insert it directly
        container.upsert_item(data)

    
def get_all_items():
    query = "SELECT * FROM c"
    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    for item in items:
        print(item)
    # return items

def send_single_message(message):

    # message = Message(json.dumps(message))
    # message.content_encoding = "utf-8"
    # message.content_type = "application/json"
    print("Sending message: {}".format(message))
    client_iot.send_message(message)
    print("Message successfully sent")
