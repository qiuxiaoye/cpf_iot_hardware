#!/bin/bash
cd ~/Code/cpf_iot_hardware || exit
echo "Stopping service at 19:00 work day..."
/usr/bin/docker compose stop

rm -f /home/CPF-IOT/Code/cpf_iot_hardware/zigbee2mqtt/data/log/*.log