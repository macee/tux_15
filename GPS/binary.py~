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
<<<<<<< HEAD
	while 1:
		data = ser.readline()
		msg_queue.put(data)
		#print data

=======
	target = open("GPS_data.txt", 'a')
	target.truncate()	
	while 1:
	
		try:
			data = ser.readline()
			msg = data.encode("HEX")
        		preamble = msg[0:6]
        		message_ID = msg[:2]
        		lat = int(msg[26:34], 16)
        		lon = int(msg[34:42], 16)
			alt = int(msg[42:50], 16)
			sea = int(msg[50:58], 16)
			line =  "{}, {}, {}".format(lat,lon, sea)
			print line
			target.write(line + "\n")
			msg_queue.put(data)
			#print data
		except:
			print "gps binary transfer error"
>>>>>>> 8cd66d00285719979817ded4a027eacc4e8c75af

def clientthread(conn):

	conn.send('Welcome to the GPS server\n')
    
	while True:
         
		line = msg_queue.get()
<<<<<<< HEAD
=======
		print '{:x}'.format(line)
>>>>>>> 8cd66d00285719979817ded4a027eacc4e8c75af
		conn.sendall(line)
     
	conn.close()
 



<<<<<<< HEAD
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
=======
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
>>>>>>> 8cd66d00285719979817ded4a027eacc4e8c75af

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
     
<<<<<<< HEAD
#	start_new_thread(clientthread ,(conn,))
 
s.close()
=======
	start_new_thread(clientthread ,(conn,))
 
s.close()
>>>>>>> 8cd66d00285719979817ded4a027eacc4e8c75af
