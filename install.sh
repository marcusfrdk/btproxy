#!/bin/bash

sudo sed -i '/dtoverlay=dwc2/d' /boot/config.txt
sudo sed -i '/dwc2/d' /etc/modules
sudo sed -i '/libcomposite/d' /etc/modules

echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules

CWD=$(dirname $(readlink -f $0))
HID_SERVICE="btproxy"
USB_SERVICE="btusb"

mkdir /tmp/$USB_SERVICE

chmod 744 $CWD/$USB_SERVICE.sh
ln -s $CWD/$USB_SERVICE.sh /usr/bin/
ln -s $CWD/$USB_SERVICE.service /etc/systemd/system/

#mkdir /tmp/$HID_SERVICE

#chmod 744 $CWD/$HID_SERVICE.py
#ln -s $CWD/$HID_SERVICE.py /usr/bin/
#ln -s $CWD/$HID_SERVICE.service /etc/systemd/system/

systemctl enable $USB_SERVICE.service
#systemctl enable $HID_SERVICE.service

echo "Please reboot to finish installation."
