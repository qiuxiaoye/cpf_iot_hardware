from flask import Flask, jsonify, send_file
import socket

from utils.config_manager import ConfigManager

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
    """
    Returns the hostname and IP address of the local machine.
    """
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return jsonify({
            "hostname": hostname,
            "ip_address": ip_address
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Unable to fetch details",
            "message": str(e)
        }), 500

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
    app.run(host='0.0.0.0', port=5001)