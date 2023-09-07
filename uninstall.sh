#!/bin/bash

HID_SERVICE="bthid"
USB_SERVICE="btusb"
CON_SERVICE="btconnect"

sudo sed -i '/dtoverlay=dwc2/d' /boot/config.txt
sudo sed -i '/dwc2/d' /etc/modules
sudo sed -i '/libcomposite/d' /etc/modules

sudo systemctl disable $USB_SERVICE.service
sudo systemctl disable $CON_SERVICE.service
sudo systemctl disable $HID_SERVICE.service

sudo systemctl daemon-reload