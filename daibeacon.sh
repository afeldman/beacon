#!/usr/bin/bash

alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'

uuid=`python -c 'import sys,uuid;sys.stdout.write(uuid.uuid4().hex)' | pbcopy && pbpaste && echo`


# see https://www.bluetooth.com/specifications/assigned-numbers/company-Identifiers for company information
dai=`echo ​0x017C`

#ID (uint8_t) - This will always be 0x02
#Data Length (uint8_t) - The number of bytes in the rest of the payload = 0x15 (21 in dec)
#128-bit UUID (uint8_t[16]) - The 128-bit ID indentifying your company/store/etc
#Major (uint16_t) - The major value (to differentiate individual stores, etc.)
#Minor (uint16_t) - The minor value (to differentiate nodes withing one location, etc.)
#TX Power (uint8_t) - This value is used to try to estimate distance based on the RSSI value

sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 3
sudo hciconfig hci0 noscan

sudo hcitool -i hci0 cmd "0x08 0x0008 1E 02 01 1A 1A FF ${dai} ${uuid} 00 00 00 00 C8"
