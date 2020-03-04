import sys
import threading
import time
import random
import socket as mysoc
from collections import defaultdict

TSdict = defaultdict(list)
# Structure of RSdict:

# TSdict = {

# 'Hostname': ['link1','link2','link3']
# 'IP Address': ['ipaddr1', 'ipaddr2','ipaddr3']
# 'Flag': ['flag1','flag2','flag3']

# }

# Structure of TSdict


def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print(err)
    server_binding=('',port)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)
# send a intro  message to the client.

    while 1:
      time.sleep(0.1)
      data = csockid.recv(1024).decode()
      if not data:
        break
      data = data.strip()
      lines = data.split('-')
      if (lines[0].strip() in TSdict.get("Hostname")):
        index = TSdict.get("Hostname").index(lines[0].strip())
        csockid.send((lines[0].strip()+" "+TSdict.get("IP Address")[index]+" "+TSdict.get("Flag")[index]).encode())
        #print((lines[0].strip()+" "+TSdict.get("IP Address")[index]+" "+TSdict.get("Flag")[index]))
      else:
        #print(lines[0].strip()," not found in TS")
        csockid.send(lines[0].strip().encode())

    ss.close()
    exit()


data = []
f = open('PROJI-DNSTS.txt','r')
while True:
  line = f.readline()
  if not line:
    break
  currline = line.strip() #gets line as words per line
  data.append(currline.split()) #separates each word in line into entries in self-generated list


filelen = len(data)

#removes last line of DNSRS where localhost is listed. appends it with tsHostname
rsf =open("PROJI-DNSRS.txt","r")
dlines=rsf.read()
rsf.close()
x=dlines.split("\n")
s="\n".join(x[:-1])
fd=open("PROJI-DNSRS.txt","w+")
for i in range(len(s)):
    fd.write(s[i])
fd.close()

#append with tsHostname at last line
host = mysoc.gethostname()
with open("PROJI-DNSRS.txt","a") as rsfile:
  rsfile.write('\n')
  rsfile.write(host + ' - NS')


for i in range(3): #traversing over HN, IPADDR, FL, populates RSDict
  for j in range(filelen):
    if i+1 == 1:
      TSdict['Hostname'].append(data[j][i].lower())
    if i+1 == 2:
      TSdict['IP Address'].append(data[j][i])
    if i+1 == 3:
      TSdict['Flag'].append(data[j][i])



#print(TSdict)


if (len(sys.argv) == 2):
  port = int(sys.argv[1])
  rsthread = threading.Thread(name='server', target=server)
  rsthread.start()

f.close()