'''
############################################################################
    AUTHOR: MAHNOOR ANJUM
    DATE CREATED: 8/31/2018
    DATE MODIFIED:  -
    DESCRIPTION: The following code implements the basic one way message
    exchange for time synchronization.


    The simplest approach of pairwise synchronization occurs when only a 
    single message is used to synchronize two nodes, that is, one node sends 
    a time stamp to another node. Here, node i sends a synchronization message
    to node j at time t1, embedding t1 as time stamp into the message. 
    Upon reception of this message, node j obtains a time stamp t2 from its own 
    local clock. The difference between the two time stamps is an indicator 
    of the clock offset.
    
    SUMMARY OF EVENTS: 
        
        Node i sends timestamp t1
        Node j receives timestamp at it's time t2
        Node j calculates t2-t1
        Node j updates it's time to t2
    
    Reference/Citation:
        Fundamentals of Wireless Sensor Networks 
        by:
            Christian Poellabauer and Waltenegus Dargie
############################################################################
'''


import time;

t1 = time.time()
#=========================== for UTC format ========================================
#import datetime
#t1 = datetime.datetime.fromtimestamp(t1).strftime('%Y-%m-%d %H:%M:%S')
#=========================== for timestamp format ==================================
t1 = str(t1)
t1 = bytearray(t1.encode())
print(t1)
# Echo server program 
import socket
 
TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 
conn, addr = s.accept()
print ('Connection address:', addr)

while 1:
     data = conn.recv(BUFFER_SIZE)
     if (data == b'0'): break
     print ("received")
     conn.send(t1)  # echo
     data = ""
     
conn.close()

    
    