#!/bin/bash

HID_SERVICE="quimby"
USB_SERVICE="btusb"
CON_SERVICE="btconnect"

sudo sed -i '/dtoverlay=dwc2/d' /boot/config.txt
sudo sed -i '/dwc2/d' /etc/modules
sudo sed -i '/libcomposite/d' /etc/modules

sudo systemctl disable $USB_SERVICE.service
sudo systemctl disable $CON_SERVICE.service
# sudo systemctl disable $HID_SERVICE.service

sudo rm /usr/bin/$USB_SERVICE.sh
sudo rm /etc/systemd/system/$USB_SERVICE.service
sudo rm -rf /tmp/$USB_SERVICE

sudo rm /usr/bin/$CON_SERVICE.sh
sudo rm /etc/systemd/system/$CON_SERVICE.service
sudo rm -rf /tmp/$CON_SERVICE

# sudo rm /usr/local/bin/$HID_SERVICE-*
# sudo rm /etc/udev/rules.d/$HID_SERVICE.rules
# sudo rm /etc/systemd/system/$HID_SERVICE.service

echo "Please reboot to finish uninstallation."