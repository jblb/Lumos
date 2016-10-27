#!/usr/bin/env python

# import lib
from source import DMXSource

import time

# data [] got the values
data = [0] * 16  # 5 rgb leds


src = DMXSource()
for i in range(256):
    data[4] = i
    src.send_data(data)
    time.sleep(0.01)
    
for i in range(256):
    data[0] = i
    data[4] = 255 -  i
    src.send_data(data)
    time.sleep(0.01)

for i in range (2):
	print ("data[%d]: %d" % (i, data[i]))
	# print("data[{}]: {}".format(i, data[i]))

for i in range(255,-1,-1):
    data[0] = i
    data[4] = 255 -  i
    src.send_data(data)
    time.sleep(0.01)

for i in range(256):
    data[4] = 255 -  i
    src.send_data(data)
    time.sleep(0.01)

for i in range (2):
	# print ("data[%d]: %d" % (i, data[i]))
	print("data[{}]: {}".format(i, data[i]))

"""
time.sleep(0.5)
data = [0] * 16
src.send_data(data)

"""

