# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:44:42 2021

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
import threading

FORMAT =  'utf-8'
DISCONNECT_MSG = "disconnect"
HEADER = 99
PORT = 5356
SERVER =  "2409:4041:2cb9:d062:5daf:b00b:9118:dba5" #socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
#create socket
socket_created = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#bind socket to address
socket_created.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_created.bind(ADDR)


def client_handling(conn,addr):
    print(f"client: {addr}\n")
    while True:
        msg_header = conn.recv(HEADER).decode(FORMAT)
        #print(msg_header)
        if msg_header:
            msg_header=int(msg_header)
            msg_actual = conn.recv(msg_header).decode(FORMAT)
            #print(msg_actual)
            if msg_actual==DISCONNECT_MSG:
                break
            data = msg_actual.split(",")
            if int(data[0])==1:
                ans = add_two_num(int(data[1]), int(data[2]))
            elif int(data[0])==2:
                ans = factorial(int(data[1]))
            else:
                ans = bin_of_dec(int(data[1]))   
            ans=str(ans)
            conn.sendall(ans.encode(FORMAT))
    #print("close")
    conn.close()            
    
def add_two_num(a,b):
    return (a+b)

def factorial(a):
    factorial = 1
    if a == 0:
       factorial=1
    else:
       for i in range(1,a + 1):
           factorial = factorial*i
    return factorial
    
def bin_of_dec(a):
    return bin(a).replace("0b","") 

def server_started():
    #server is started and listening
    socket_created.listen()
    while True:
        conn, addr = socket_created.accept()  
        thread = threading.Thread(target=client_handling,args=(conn, addr))
        thread.start()
print(f"server started at {SERVER}\n")
server_started()