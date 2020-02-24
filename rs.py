import sys
import threading
import time
import random
import socket as mysoc

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

    ss.close()
    exit()


if (len(sys.argv) == 2):
    if(sys.argv[1] == "rsListenPort"):
        rsthread = threading.Thread(name='server', target=server)
        rsthread.start()
