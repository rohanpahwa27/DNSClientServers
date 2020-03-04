#client task
import sys
import threading
import time
import random
import socket as mysoc
from collections import defaultdict

CLdict = defaultdict(list)
# Structure of CLdict:

# CLdict = {
# 'Hostname': ['link1','link2','link3']
# }

# Structure of CLdict

def client():
    #connect to rs socket
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print(err)

 # Define the port on which you want to connect to the server
    port = rsport
    sa_sameas_myaddr =mysoc.gethostbyname(host)
 # connect to the server on local machine
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)



    #connect to ts socket
    #try:
        #ts=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        #print("[C]: Client socket created")
    #except mysoc.error as err:
        #print(err)
    #port = tsport
    #tsa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
 # connect to the server on local machine
    #tsserver_binding=(tsa_sameas_myaddr,port)
    #ts.connect(tsserver_binding)





    data_from_server=cs.recv(100)
 #receive data from the server

    print("[C]: Data received from server::  ",data_from_server.decode('utf-8'))

    #sends length of strings to send to root server to check if its there
    cs.send(str(len(CLdict.get('Hostname'))).encode())
    
    datasent = ""
    tscon = False
    #sends actual strings to root server (line by line)
    f = open("RESOLVED.txt", "a")
    for j in range(len(CLdict.get('Hostname'))):
        datasent = CLdict.get('Hostname')[j]
        cs.send(datasent.encode('utf-8'))
        time.sleep(0.1)
        data = cs.recv(1024).decode()
        if (data[len(data)-1] == 'A'):
            #print(CLdict.get('Hostname')[j],"received")
            f.write(data+"\n")
        else:
            if tscon == False:
            #connect to ts server if tscon = false (if ts server not connected already)
                try:
                    ts=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
                    print("[C]: Client socket created")
                except mysoc.error as err:
                    print(err)
                port = tsport
                tsa_sameas_myaddr =mysoc.gethostbyname(data)
                # connect to the server on local machine
                tsserver_binding=(tsa_sameas_myaddr,port)
                ts.connect(tsserver_binding)
            tscon = True
            #print(CLdict.get('Hostname')[j])
            ts.send(datasent.encode())
            time.sleep(0.1)
            data = ts.recv(1024).decode()
            lines = data.split()
            if (len(lines) == 1):
                f.write(data+" - Error:HOST NOT FOUND"+"\n")
            else:
                f.write(data+"\n")
            #print("-----------", lines)
            
            

    ts.close()
    cs.close()
    exit()

data = []
f = open('PROJI-HNS.txt','r')
while True:
  line = f.readline()
  if not line:
    break
  currline = line.strip() #gets line as words per line
  data.append(currline.split()) #separates each word in line into entries in self-generated list


filelen = len(data)

 #traversing over HN
for j in range(filelen):
  CLdict['Hostname'].append(data[j][0].lower())

# for j in range(len(CLdict.get('Hostname'))):
#     print(CLdict.get('Hostname')[j])


# print(CLdict)


if (len(sys.argv) == 4):
    host = sys.argv[1]
    rsport = int(sys.argv[2])
    tsport = int(sys.argv[3])
    rsthread = threading.Thread(name='client', target=client)
    rsthread.start()
        # input("Hit ENTER  to exit")
# exit()