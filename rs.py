import sys
import threading
import time
import random
import socket as mysoc
from collections import defaultdict


RSdict = defaultdict(list)
# Structure of RSdict:

# RSdict = {

# 'Hostname': ['link1','link2','link3']
# 'IP Address': ['ipaddr1', 'ipaddr2','ipaddr3']
# 'Flag': ['flag1','flag2','flag3']

# }

# Structure of RSdict



# server task
def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print(err)
    server_binding=('',52799)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)
# send a intro  message to the client.
    msg="Welcome to CS 352"
    csockid.send(msg.encode('utf-8')) 

    #gets length of strings being sent by client
    lenth_of_client = int(csockid.recv(1).decode())

    #prints out the data received from client
    for j in range(lenth_of_client):
        #print(RSdict.get('Hostname')[j])
        data = csockid.recv(24).decode()
        print ("hi",data,"hi")

    ss.close()
    exit()




data = []
f = open('PROJI-DNSRS.txt','r')
while True:
  line = f.readline()
  if not line:
    break
  currline = line.strip() #gets line as words per line
  data.append(currline.split()) #separates each word in line into entries in self-generated list


filelen = len(data)

for i in range(3): #traversing over HN, IPADDR, FL, populates RSDict
  for j in range(filelen):
    if i+1 == 1:
      RSdict['Hostname'].append(data[j][i])
    if i+1 == 2:
      RSdict['IP Address'].append(data[j][i])
    if i+1 == 3:
      RSdict['Flag'].append(data[j][i])

# print(RSdict)


# how to read a text file in python
# with open("PROJI-DNSRS.txt") as f:
#   while True:
#     c = f.read(1)
#     print("".join(["EOF: ", c]))
#     if not c:
#       print ("End of file")
#       break
#     print ("".join(["Read a character:",c," ","hi"]))
if (len(sys.argv) == 2):
    if(sys.argv[1] == "rsListenPort"):
        rsthread = threading.Thread(name='server', target=server)
        rsthread.start()
