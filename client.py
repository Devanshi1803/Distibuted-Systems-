# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:18:18 2021

@author: devanshi
"""
"""
1. Write a Java program such that:
i) The client program fetches user’s choice for adding two numbers, or
calculating factorial of a number , or finding binary of a decimal input. As per
choice user input is also fetched.
ii) Client sends the input to the server.
iii) Server calculates and returns the necessary value as per user’s choice (e.g., if
user had requested for adding two numbers server will calculate sum and
return it to the client)
"""

import socket

HEADER = 99
DISCONNECT_MSG = "disconnect"
FORMAT =  'utf-8'
PORT = 5356
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
#create socket
socket_created = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#connect to server
socket_created.connect(ADDR)

def sendmsg(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER-len(send_len)) 
    socket_created.send(send_len)
    socket_created.send(message)
    

print("1) Add two numbers\n2) Factorial of number\n3) Binary of decimal\n")
while(1):
    choice = int(input("Enter your choice: "))
    if choice==1:
        n1=int(input("Enter num1: "))
        n2=int(input("Enter num2: "))
        msg = ",".join([str(choice),str(n1),str(n2)])
        break
    elif choice==2:
        while(1):
            n1=int(input("Enter number: "))
            if n1>=0:
                break
            else:
                print("Please Enter positive number")
        msg = ",".join([str(choice),str(n1)])
        break
    elif choice==3:
        n1=int(input("Enter number: "))
        msg = ",".join([str(choice),str(n1)])
        break
    else:
        print("Invalid choice")
        
sendmsg(msg)
ans = socket_created.recv(HEADER).decode(FORMAT)
print("\nAnswer : "+ans)
sendmsg(DISCONNECT_MSG)