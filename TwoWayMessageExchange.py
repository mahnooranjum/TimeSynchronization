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
############################# SERVER #######################################

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
BUFFER_SIZE = 2024  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 
conn, addr = s.accept()
print ('Connection address:', addr)

while 1:
     data = conn.recv(BUFFER_SIZE)
     if (data == b'0'): break
     print (data)
     conn.send(t1)  # echo
     data = ""
     
conn.close()