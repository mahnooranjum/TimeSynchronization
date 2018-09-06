'''
############################################################################
    AUTHOR: MAHNOOR ANJUM
    DATE CREATED: 8/31/2018
    DATE MODIFIED:  -
    DESCRIPTION: The following code implements the two way message
    exchange for time synchronization.


    A somewhat more accurate approach is to use two synchronization messages. 
    Here, node j responds with a message issued at time t3,
    containing time stamps t1, t2, and t3. Upon reception of this second message at time t4,
    both nodes are able to determine the clock offset, again assuming a fixed value for the
    propagation delay. However, node i is now able to more accurately determine both the
    propagation delay and the offset
    
    SUMMARY OF EVENTS: 
        
        Node i sends timestamp t1
        Node j receives timestamp at it's time t2
        Node j calculates t2-t1
        Node j updates it's time to t2
        
        Node j transmits timstamp at t3
        Node i receives timestamp at t4
        Node i calculates:
            delay = ((t4-t3) + (t2-t1)) /2
            offset = ((t2-t1) - (t4-t3)) /2
               
    Reference/Citation:
        Fundamentals of Wireless Sensor Networks 
        by:
            Christian Poellabauer and Waltenegus Dargie
        
############################################################################
############################# CLIENT #######################################
'''
import socket
import time
import datetime
TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 4096
MESSAGE = "Connection Established"
def set_time():
    pass
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytearray(MESSAGE.encode()))
while(1):
    MESSAGE = input()
    s.send(bytearray(MESSAGE.encode()))
    t1 = s.recv(BUFFER_SIZE)
    t2 = time.time()
    t1 = t1.decode("utf-8")
    if(t1.count('.')==1):
        t1 = float(t1)
        tdif = float(t2) - t1
        if(tdif==0):
            print("Synchronized")
        else:
            set_time()
        print("t1: ", t1) 
        print("t2: ", t2)
        t3 = time.time()
        s.send(bytearray(" t1: ".encode()))
        s.send(bytearray(str(t1).encode()))
        s.send(bytearray(" t2: ".encode()))
        s.send(bytearray(str(t2).encode()))
        s.send(bytearray(" t3: ".encode()))
        s.send(bytearray(str(t3).encode()))
    else:
        print("Two decimals? Really?")
    t1=0
    t2=0
    t3=0
    
s.close()
 

