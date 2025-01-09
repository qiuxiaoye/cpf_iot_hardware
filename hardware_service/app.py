from flask import Flask, jsonify, send_file
import socket
import logging

from utils.config_manager import ConfigManager
from utils.telegram_message import Telegram_Message
from utils.retrieve_ip import IPFetcher

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

HOST_NAME = socket.gethostname()
# IP_ADDRESS = IPFetcher.get_interface_ip("enp1s0") # testing at home
IP_ADDRESS = IPFetcher.get_interface_ip("wlan0") # testing at work

def send_ip_on_startup():
    """
    Sends the IP address and HOST_NAME to Telegram on app startup.
    """
    try:

        # Call the Telegram script
        Telegram_Message().send_ip_to_telegram(HOST_NAME, IP_ADDRESS)
        print(f"IP and HOST_NAME sent to Telegram: {HOST_NAME}, {IP_ADDRESS}")
    except Exception as e:
        print(f"Error sending IP to Telegram: {e}")

# Get configuation file for zigbee2mqtt
@app.route('/get-zigbee2mqtt-config', methods=['GET'])
def get_config():
    config_file_path = "configuration.yaml"
    config_manager = ConfigManager(config_file_path)
    config_manager.create_default_config()
    
    # Path to the configuration file
    file_path = "configuration.yaml"
    
    # Serve the file to the user
    try:
        return send_file(file_path, as_attachment=True, download_name="configuration.yaml")
    except FileNotFoundError:
        return "Configuration file not found!", 404

if __name__ == '__main__':
    send_ip_on_startup()
    app.run(host='0.0.0.0', port=5001)