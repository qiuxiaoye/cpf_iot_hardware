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

