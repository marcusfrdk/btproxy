#!/usr/bin/env python3

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name', type=str)
args = parser.parse_args()

name = args.name
root = os.path.join('/sys/kernel/config/usb_gadget/', name)

# Follows the cleanup routine outlined in:
#   https://www.kernel.org/doc/Documentation/usb/gadget_configfs.txt

for config in os.scandir(f"{root}/configs"):
    # rm configs/<config name>.<number>/<function>
    for function in os.scandir(config.path):
        if function.is_symlink():
            os.remove(function.path)

    # rmdir configs/<config name>.<number>/strings/<lang>
    for lang in os.scandir(f"{config.path}/strings/"):
        os.rmdir(lang.path)

    # rmdir configs/<config name>.<number>
    os.rmdir(config.path)

# rmdir functions/<name>.<instance name>
for function in os.scandir(f"{root}/functions/"):
    os.rmdir(function.path)

# rmdir strings/<lang>
for strings in os.scandir(f"{root}/strings/"):
    os.rmdir(strings.path)

# rmdir <gadget name>
os.rmdir(root)
