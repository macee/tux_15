'''
    Simple socket server using threads
'''

import serial
import threading
import Queue
 
import socket
import sys
from thread import *


def readserialthread():
	while 1:
		data = ser.readline()
		msg_queue.put(data)
		#print data


def clientthread(conn):

	conn.send('Welcome to the GPS server\n')
    
	while True:
         
		line = msg_queue.get()
		conn.sendall(line)
     
	conn.close()
 



ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

msg_queue = Queue.Queue(1024)
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

event = threading.Event()

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
 

 
 

start_new_thread(readserialthread,() )


while 1:
 
	conn, addr = s.accept()

	print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
#	start_new_thread(clientthread ,(conn,))
 
s.close()