#!/usr/bin/python

import sys,uuid,re
import subprocess,os

debug = True

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

print("Launching virtual iBeacon...")
os.system("sudo hciconfig %s up" % hci_device)
os.system("sudo hciconfig %s noleadv" % hci_device)
os.system("sudo hciconfig %s leadv 3" % hci_device)
os.system("sudo hciconfig %s noscan" % hci_device)
print("done config")

print("start subprocess :")
subprocess.call(("sudo hcitool -i %s cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 %s %s %s %s" % (hci_device,getuuid(), major, minor, power)), shell=True)

print("Complete")
