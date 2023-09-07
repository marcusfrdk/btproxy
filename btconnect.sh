#!/bin/bash

DEVICE_ADDRESS="5C:E9:1E:0A:C0:5F"

if [ -z "$DEVICE_ADDRESS" ]; then
    echo "Please set DEVICE_ADDRESS variable in this script."
    exit 1
fi

echo -e "connect $DEVICE_ADDRESS\nexit" | bluetoothctl
echo "Connected to $DEVICE_ADDRESS"