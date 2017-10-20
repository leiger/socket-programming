# UDPPingerClient.py
from socket import *
import time

# set server name and server port name
serverName = '127.0.0.1'
serverPort = 12000

ping_times = 10

# create the client's socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(0, ping_times):
    try:
        # sending time
        start_time = time.time()
        # send the resulting packet into the destination address
        clientSocket.sendto('d'.encode('utf-8'), (serverName, serverPort))
        # client socket waiting time
        clientSocket.settimeout(2.0)
        # modifiedMessage: receive the message from serverClient
        # serverAddress: server's IP address and server's port
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        # receiving time
        end_time = time.time()
        # round trip time
        RTT_time = end_time - start_time
        print("Ping  %d  %.3f" %(i+1, RTT_time))
        print("Response message:", modifiedMessage.decode())

    except timeout:
        print("Ping  %d  Request timed out" %(i+1))

clientSocket.close()