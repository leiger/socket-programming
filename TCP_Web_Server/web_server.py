# import socket module
from socket import *
import threading,time

# the server creates a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
serverSocket.bind(('127.0.0.1', 6789))

# the server listen for TCP connection requests from the client.
# The parameter specifies the maximum number of queued connections
serverSocket.listen(5)
print('Ready to serve...')

def tcpLink(connectionSocket, addr):
    print('Accept new connection from %s:%s...' % addr)
    # Establish the connection
    try:
        message = connectionSocket.recv(1024)
        print(message)
        # get URL
        filename = message.split()[1]
        f = open(filename[1:])
        # print(filename)
        # read by lines
        outputdata = f.readlines()
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.send('404 Not Found'.encode())
        # Close client socket
        connectionSocket.close()

while True:
    # create a new socket in the server, called connectionSocket
    connectionSocket, addr = serverSocket.accept()
    # create a separate thread
    t = threading.Thread(target=tcpLink, args=(connectionSocket, addr))
    t.start()

serverSocket.close()
sys.exit()