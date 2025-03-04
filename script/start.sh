#!/bin/bash
cd ~/Code/cpf_iot_hardware || exit
echo "Starting message_router at 8am every work day..."
/usr/bin/docker compose start message_router