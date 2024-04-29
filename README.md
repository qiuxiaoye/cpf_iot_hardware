# IOT PROJECT

This CPF IOT Project is for raspberry pi installation. It helps IOT software to be quicklly deployed to raspberry pi.

Present sensor collect the human presence data from MMwave Sensor. Data was transmitted using `MQTT` and received by raspberry pi using zigbee dongle. Raspberry Pi capture data using `Zigbee2mqtt` and `paho` and upload data into Azure Cosmos db.

All software installation is pre-configed by `docker-compose`

## Hardware Requirements
1. Plug in Power
2. Plug in MicroSD Card
3. plug in Zigbee Dongle

## Software Requirements
1. Install Raspberry Pi OS
2. Raspberry Pi Account Setup (optional)
3. Install Docker and Docker Compose

## Command
sudo docker-compose up -d --build

sudo docker-compose up -d
sudo docker-compose down


## Raspberry Pi Configurations
1. Keep Pi Always On. (Under Testing.....)
    https://chat.openai.com/c/11389311-64a6-4017-9177-6c69a0725af0
    First, update your EEPROM firmware to the latest version:
        sudo apt update
        sudo apt full-upgrade
        sudo rpi-eeprom-update -a
        sudo reboot
    Then, configure the EEPROM to set the power-on behavior:
        sudo -E rpi-eeprom-config --edit
    In the editor, look for the POWER_OFF_ON_HALT setting and change it to:
        POWER_OFF_ON_HALT=0
        WAKE_ON_GPIO=1
    Save and exit the editor, and then apply the changes:





