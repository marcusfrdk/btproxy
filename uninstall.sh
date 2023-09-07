#!/bin/bash

HID_SERVICE="btproxy"
USB_SERVICE="btusb"

sudo sed -i '/dtoverlay=dwc2/d' /boot/config.txt
sudo sed -i '/dwc2/d' /etc/modules
sudo sed -i '/libcomposite/d' /etc/modules

sudo rm /usr/bin/$USB_SERVICE.sh
sudo rm /etc/systemd/system/$USB_SERVICE.service
sudo rm -rf /tmp/$USB_SERVICE

#sudo rm /usr/bin/$HID_SERVICE.py
#sudo rm /etc/systemd/system/$HID_SERVICE.service
#sudo rm -rf /tmp/$HID_SERVICE

sudo systemctl disable $USB_SERVICE.service
#sudo systemctl disable $HID_SERVICE.service

echo "Please reboot to finish uninstallation."