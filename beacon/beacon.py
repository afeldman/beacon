#!/usr/bin/python

import sys
import uuid
import re
import subprocess
import os

def check_user():
    if not (os.getuid() == 0):
        print ("you are not sudo")
        sys.exit()

def check_device(device):
    try:
        subprocess.call(["hciconfig","help"])
    except OSError as e:
        print ("Install bluez")
        sys.exit()

def getuuid():
    _uuid = uuid.uuid4().hex
    re_uuid = re.findall('..?',str(_uuid))

    return ' '.join(re_uuid)
        
class Beacon:

    major = "00 00"
    minor = "00 00"
    power = "C5 00"
    
    def __init__(self, device = "hci0"):
        self.hci_device = device


    def config(self):
        os.system("hciconfig %s up" % self.hci_device)
        os.system("hciconfig %s noleadv" % self.hci_device)
        os.system("hciconfig %s leadv 3" % self.hci_device)
        os.system("hciconfig %s noscan" % self.hci_device)


    def start(self,one,two):
        try:
            subprocess.call(("sudo hcitool -i %s cmd 0x08 0x0008 1E 02 01 1A 1A FF %s %s 02 15 %s %s %s %s" % (self.hci_device, one, two, getuuid(), self.major, self.minor, self.power)), shell=True)

            return 0
        except OSError as e:
            return 1
