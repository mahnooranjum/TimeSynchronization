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
import socket
import time
import datetime
TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 1024
MESSAGE = "Connection Established"

def set_time(systime):
    pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytearray(MESSAGE.encode()))
while(1):
    MESSAGE = input()
    s.send(bytearray(MESSAGE.encode()))
    data = s.recv(BUFFER_SIZE)
    t2 = time.time()
    print ("received:", data)
    data = data.decode("utf-8")
    if(data.count('.')==1):
        data = float(data)
        print (type(data))
        tdif = float(t2) - data
        if(tdif==0):
            print("Synchronized")
        else:
            systime = datetime.datetime.fromtimestamp(data).strftime
            ('%Y-%m-%d %H:%M:%S')
            set_time()
        
    
s.close()
 



