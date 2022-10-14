
import socket 
serverName = 'localhost'
serverPort=3000
clientSocket = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)
message = input('Input lowercase sentence :')
clientSocket.sendto(message.encode("UTF-8"),(serverName,serverPort))
date , clientAddress = clientSocket.recvfrom((2048))
print( date.decode('UTF-8'))
clientSocket.close()
message = input('press enter to exit')
