'''
    GPS socket server
'''
# FIXME We should be able to serve the same data to multiple clients. While many clients can 
# connnect to this server they do not share the queue properly. consiquently, each client sees 
# only a portion of the data...


import threading
import Queue
 
import socket
import sys
import time
from thread import *


def readserialthread():
    
	cnt = 1;

	while True:
		msg = "Hello World " + str(cnt) + "\n"
		msg_queue.put(msg)
		cnt = cnt + 1;
		time.sleep(0.5)



def clientthread(conn):

	conn.send('Welcome to the GPS server\n')
#	msg_queue.join()

	while True:
		line = msg_queue.get()
		conn.sendall(line)
	conn.close()
 


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
      
start_new_thread(readserialthread,() )
   
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
while 1:
 
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	start_new_thread(clientthread ,(conn,))

s.close()