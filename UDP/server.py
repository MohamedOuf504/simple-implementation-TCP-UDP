import socket
serverPort = 3000
serverSocket = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The Server Up and Running')

while True:
    date , clientAddress = serverSocket.recvfrom((2048))
    message = date.decode('UTF-8')
    print(message)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage.encode("UTF-8"),clientAddress)