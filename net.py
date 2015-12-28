#code:UTF-8
import json
import time
import socket
import os
import sys
import threading

KEY = "xiaoqingxinchunjieshanliang"

#The thread which send data to the remote server to keep the connection
class ConnectionThread(threading.Thread):
    def __init__(self, udp, serverAddress):
        threading.Thread.__init__(self)
        self.connectData = json.dumps({"action":"connect", "key":"xiaoqingxin"})
        self.udp = udp
        self.serverAddress = serverAddress

    def connectServer(self):
        print "Connecting to server..."
        self.udp.sendto(self.connectData, self.address)
        
    def run(self):
        while(True):
            self.connectServer()
            time.sleep(10)

#init the udp socket
def initSocket(port):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("", port))
    print "UDP socket created, listening on the port: " + str(port) + "\n"
    return udp

#handle the request received form the port
def handleRequest(udp):
    while(True):
        jsonStr = udp.recv(1024)
        data = json.loads(jsonStr)
        try:
            if(data["key"] == KEY):
                if(data["action"] == "open"):
                    print "open"
                elif(data["action" == "close"]):
                    print "close"
        except KeyError:
            print "Key error"

if __name__ == "__main__":
    global raspPort
    global serverIp
    global serverPort
    if(len(sys.argv)!= 4):
        print "Usage: python net.py raspPort serverIp serverPort"
        exit(1)
    raspPort = int(sys.argv[1])
    serverIp = sys.argv[2]
    serverPort = int(sys.argv[3])
    udp = initSocket(raspPort)
    handleRequest(udp)
    connectionThread = ConnectionThread(udp, (serverIp, serverAddress))
    connectionThread.start()
