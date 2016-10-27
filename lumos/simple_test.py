#!/usr/bin/env python

# from packet import E131Packet
from source import DMXSource

# import socket
# import struct
import time


data = [0] * 16

# p = E131Packet(universe=1, data=data)
# print p.packet


# 239.256.0.1:5568
# UDP_IP = "239.255.0.1"
# UDP_IP = "127.0.0.1"
# UDP_PORT = 5568
# multicast_group = ("239.255.0.1", 5568)

# sock = socket.socket(socket.AF_INET, # Internet
#                      socket.SOCK_DGRAM) # UDP

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
# ttl = struct.pack('b', 1)


# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
# sock.settimeout(0.2)

# sent = sock.sendto(p.packet, (UDP_IP, UDP_PORT))
src = DMXSource()


for i in range(255):
    data[0] = i
    data[4] = 255 -  i
    src.send_data(data)
    time.sleep(0.1)
    print(".")

print("***************************************")
data = [0] * 500
src.send_data(data)
