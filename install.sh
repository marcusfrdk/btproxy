#!/bin/bash

sudo sed -i '/dtoverlay=dwc2/d' /boot/config.txt
sudo sed -i '/dwc2/d' /etc/modules
sudo sed -i '/libcomposite/d' /etc/modules

echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules

CWD=$(dirname $(readlink -f $0))
HID_SERVICE="bthid"
USB_SERVICE="btusb"
CON_SERVICE="btconnect"

# USB Gadget Service
if [ ! -f /etc/systemd/system/$USB_SERVICE.service ]; then
    echo "Installing '$USB_SERVICE' service..."
    ln -s $CWD/$USB_SERVICE.service /etc/systemd/system/
else
    echo "'$USB_SERVICE' service already installed, skipping..."
fi

# Auto-connect to device
if [ ! -f /etc/systemd/system/$CON_SERVICE.service ]; then
    echo "Installing '$CON_SERVICE' service..."
    ln -s $CWD/$CON_SERVICE.service /etc/systemd/system/
else
    echo "'$CON_SERVICE' service already installed, skipping..."
fi

# HID
if [ ! -f /etc/systemd/system/$HID_SERVICE.service ]; then
    echo "Installing '$HID_SERVICE' service..."
    ln -s $CWD/$HID_SERVICE.service /etc/systemd/system/
else
    echo "'$HID_SERVICE' service already installed, skipping..."
fi

systemctl enable $USB_SERVICE.service
systemctl enable $CON_SERVICE.service
systemctl enable $HID_SERVICE.service
