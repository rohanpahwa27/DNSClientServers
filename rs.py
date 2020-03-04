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
    server_binding=('',int(port))
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

    CLdata = []
    #prints out the data received from client
    for j in range(lenth_of_client):
        data = csockid.recv(1024).decode()
        lines = data.strip().lower()
        if(lines in RSdict.get("Hostname")):
          index = RSdict.get("Hostname").index(lines)
          csockid.send((lines+" "+RSdict.get("IP Address")[index]+" "+RSdict.get("Flag")[index]).encode())
        else: #send tsHostname back to client 
          tsHostname = RSdict["Hostname"][filelen-1]
          csockid.send(tsHostname.encode())
        # time.sleep(.1)


    # print(CLdata)
    #for i in range (len(CLdata)):
        #if(CLdata[i] in RSdict.get("Hostname")):
          #index = RSdict.get("Hostname").index(CLdata[i])
          #f = open("RESOLVED.txt", "a")
          #f.write(CLdata[i]+ " "+RSdict.get("IP Address")[index]+" "+RSdict.get("Flag")[index]+"\n")
        #else:
          #csockid
        # else: go back to client with a string to lookup in ts.py but will have to open that socket too
            
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
      if j+1 == filelen:
        RSdict['Hostname'].append(data[j][i]) #last entry isn't lower case due to tsHostname
      else:  
        RSdict['Hostname'].append(data[j][i].lower())
    if i+1 == 2:
      RSdict['IP Address'].append(data[j][i])
    if i+1 == 3:
      RSdict['Flag'].append(data[j][i])



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
  port = sys.argv[1]
  rsthread = threading.Thread(name='server', target=server)
  rsthread.start()
