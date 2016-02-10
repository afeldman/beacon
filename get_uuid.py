#!/usr/bin/python

import sys,uuid,re

_uuid = uuid.uuid4().hex

re_uuid = re.findall('..?',str(_uuid))

print re_uuid
