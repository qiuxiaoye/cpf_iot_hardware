#!/bin/bash

# Get the IP address of wlan0
HOST_WLAN0_IP=$(ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
echo "Detected HOST_WLAN0_IP: $HOST_WLAN0_IP"

# Export the IP address as an environment variable for docker-compose
export HOST_WLAN0_IP

# Run docker-compose with the environment variable
docker-compose up -d