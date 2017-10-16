from socket import *
import sys

# print(sys.argv)
#get input command format
webServer = sys.argv[1]
webPort = int(sys.argv[2])
webURL = sys.argv[3]

get_str = '''GET /%s HTTP/1.1\r
Host: %s:%s\r
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36\r
Accept: */*\r\n\r\n'''

# AF_INET: IPV4; SOCK_STREAM: TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# 完成三次握手
clientSocket.connect((webServer, webPort))

clientSocket.send((get_str % (webURL, webServer, webPort)).encode())
# Characters continue to accumulate until the line ends with a carriage return character.
response = ''
serverContent = clientSocket.recv(1024)
print(serverContent.decode())
while serverContent:
    serverContent = clientSocket.recv(1024)
    response += serverContent.decode()

print(response)
clientSocket.close()