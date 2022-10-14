from email import message
import socket 
host ='localhost'
serverPort=3000
clientSocket = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
clientSocket.connect((host,serverPort))
data = clientSocket.recv(1024)
if len(data):
    print('Received:' , data.decode('utf-8'))
    data = "message goes here"
while len(data):
    message= input('Input lowercase sentence (type quit to end communication) :')
    clientSocket.send(message.encode('utf-8'))
    data = clientSocket.recv(1024)
    print('Received:' , data.decode('utf-8'))
    if message =='quit':
        data=''
clientSocket.close()