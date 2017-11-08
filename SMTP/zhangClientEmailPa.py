from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', 587)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


tls = "STARTTLS\r\n".encode()
clientSocket.send(tls)
recv1 = clientSocket.recv(1024).decode()
print(recv1)
clientSocket = ssl.wrap_socket(clientSocket)

clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print(recv1)

#username and password
username = input("USERNAME:")
password = input("PASSWORD:")
base64_str = ('\x00' + username + '\x00' + password).encode()
base64_str = base64.b64encode(base64_str)
base64_str = base64_str.strip("\n".encode())
#auth = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv1 = clientSocket.recv(1024)
print("After auth: "+recv1.decode())



# Send MAIL FROM command and print server response.
clientSocket.send('MAIL FROM:<leiger2017@gmail.com>\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print('MAIL:', recv1)
if recv1[:3] != '250':
    print('mail 250 reply not received from server.')

# Send RCPT TO command and print server response.
clientSocket.send('RCPT TO:<1120720058@qq.com>\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print('RCPT:', recv1)
if recv1[:3] != '250':
    print('rcpt 250 reply not received from server.')

# Send DATA command and print server response.
clientSocket.send('DATA\r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print('DATA:', recv1)
if recv1[:3] != '354':
    print('data 354 reply not received from server.')

# Send message data.
clientSocket.send('Subject: hahaha\r\n\r\n'.encode())
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024).decode()
print('endmsg:', recv1)
if recv1[:3] != '250':
    print('end msg 250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
recv1 = clientSocket.recv(1024).decode()
print('quit:', recv1)
if recv1[:3] != '250':
    print('quit 250 reply not received from server.')

clientSocket.close()