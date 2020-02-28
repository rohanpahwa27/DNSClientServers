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
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print(err)

# Define the port on which you want to connect to the server
    port = 52799
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
# connect to the server on local machine
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)

    data_from_server=cs.recv(100)
#receive data from the server

    print("[C]: Data received from server::  ",data_from_server.decode('utf-8'))

    #sends length of strings to send to root server to check if its there
    cs.send(str(len(CLdict.get('Hostname'))).encode())

    #sends actual strings to root server (line by line)
    for j in range(len(CLdict.get('Hostname'))):
        print(CLdict.get('Hostname')[j])
        cs.send(CLdict.get('Hostname')[j].encode())
    

    
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
  CLdict['Hostname'].append(data[j][0])

# for j in range(len(CLdict.get('Hostname'))):
#     print(CLdict.get('Hostname')[j])


# print(CLdict)


if (len(sys.argv) == 4):
    if (sys.argv[1] == "rsHostname" and sys.argv[2] == "rsListenPort" and sys.argv[3] == "tsListenPort"):
        cthread = threading.Thread(name='client', target=client)
        cthread.start()
        input("Hit ENTER  to exit")
# exit()