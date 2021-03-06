# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
import time
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

CHECK_TIME = 10
start = 0
receiveTime = []
currentTime = []

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    # Capitalize the message from the client
    receiveTime.append(message.decode())

    if start != 0:
        currentTime.append(time.time())
        delayTime = currentTime[1] - float(receiveTime[0])
        print(delayTime)
        if (delayTime > CHECK_TIME):
            print('The client application has stopped.')
        else:
            print('The client is running.')

        currentTime.pop(0)
        receiveTime.pop(0)

    start += 1

    # message = message.upper()
    # If rand is less is than 3, we consider the packet lost and do not respond
    if rand < 3:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)