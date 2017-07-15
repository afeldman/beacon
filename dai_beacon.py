#!/usr/bin/python

# you have to install bluez

import sys,uuid,re
import subprocess,os

debug = True

# make sure bluez is installed und running

hci_device = "hci0"
major = "00 00"
minor = "00 00"
power = "C5 00"

if len(sys.argv) == 2:
    hci_device = sys.argv[1]
else:
    hci_device = "hci0"

if debug:
    print(hci_device)

def getuuid():
    _uuid = uuid.uuid4().hex
    re_uuid = re.findall('..?',str(_uuid))

    return ' '.join(re_uuid)

# broadcast the device
print("Launching virtual Dai_Beacon...")
os.system("sudo hciconfig %s up" % hci_device)
os.system("sudo hciconfig %s noleadv" % hci_device)
os.system("sudo hciconfig %s leadv 3" % hci_device)
os.system("sudo hciconfig %s noscan" % hci_device)
print("done config")

# FF 01 7c behind the FF comse the company number. Daimler AG is 0x017c
print("start sending protocoll :")
# 1E 02 01 1A 1A FF 01 7c 02 15 Beacon prefix Manifacturer data beginns with ff
# followed by the uuid of this device
# followed by the major
# the minor
# and the tx power value
subprocess.call(("sudo hcitool -i %s cmd 0x08 0x0008 1E 02 01 1A 1A FF 01 7c 02 15 %s %s %s %s" % (hci_device, getuuid(), major, minor, power)), shell=True)

print("Complete")
