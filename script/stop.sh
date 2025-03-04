#!/bin/bash
cd ~/Code/cpf_iot_hardware || exit
echo "Stopping message_router at 19:00 work day..."
/usr/bin/docker compose stop message_router