# UDPPingerClient.py
from socket import *
from numpy import max, min, mean, std
from matplotlib import pyplot
import time

# set server name and server port name
serverName = '127.0.0.1'
serverPort = 12000

ping_times = 10

# packet loss rate
pkt_loss_rate = 0

# successful times
success_ping = []

#beat period
BEAT_PERIOD = 5

# create the client's socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(0, ping_times):
    try:
        # sending time
        start_time = time.time()
        # send the resulting packet into the destination address
        clientSocket.sendto(str(start_time).encode('utf-8'), (serverName, serverPort))
        # client socket waiting time
        clientSocket.settimeout(2.0)
        # modifiedMessage: receive the message from serverClient
        # serverAddress: server's IP address and server's port
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        # receiving time
        end_time = time.time()
        # round trip time
        RTT_time = end_time - start_time
        print("Ping %d %f" %(i+1, RTT_time))

        success_ping.append(RTT_time)

        # sleep time
        time.sleep(BEAT_PERIOD)

    except timeout:
        print("Request timed out")


# get packet loss rate
pkt_loss_rate = (ping_times-len(success_ping))/ping_times*100

# histogram info
def drawHist(data):
    pyplot.hist(data)
    pyplot.xlabel('RTTs')
    pyplot.ylabel('num')
    pyplot.text(0.0001, 10, '')
    pyplot.title('Histogram of RTTs')
    pyplot.show()

print("====================")
print("minimum RTT: %f" %(min(success_ping)))
print("maximum RTT: %f" %(max(success_ping)))
print("average RTT: %f" %(mean(success_ping)))
print("standard deviation RTT: %f" %(std(success_ping)))
print("====================")
print("packet loss rate: %f%%" %(pkt_loss_rate))
print("====================")
drawHist(success_ping)
# print(success_ping)

clientSocket.close()