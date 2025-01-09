class ConfigManager:
    """Handles configuration file operations."""
    
    def __init__(self, file_path):
        self.file_path = file_path

    def create_default_config(self):
        """Creates the default configuration file if it doesn't exist."""
        default_content = """homeassistant: false
                            permit_join: true
                            mqtt:
                            base_topic: zigbee2mqtt
                            server: mqtt://mosquitto
                            serial:
                            port: /dev/ttyUSB0
                            frontend:
                            port: 8080
                            devices:
                            '0x54ef44100064b0cb':
                                friendly_name: test_device_1
                            '0x54ef441000811c36':
                                friendly_name: test_device_2
                            '0x54ef441000e294af':
                                friendly_name: '0x54ef441000e294af'
                            advanced:
                            homeassistant_legacy_entity_attributes: false
                            legacy_api: false
                            legacy_availability_payload: false
                            device_options:
                            legacy: false
                            """
        try:
            with open(self.file_path, "x") as file:  # Use "x" mode to ensure it doesn't overwrite
                file.write(default_content)
        except FileExistsError:
            # File already exists, do nothing
            pass

    def get_file_path(self):
        """Returns the file path of the configuration file."""
        return self.file_path