import socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',3000)
print ('The Server Up and Running' , server_address)
sock.bind(server_address)


sock.listen(1)

while True:
    print ('Waiting for a connection')
    connection,client_address =sock.accept()
    try:
        print ('client connected:', client_address)
        connection,client_address =sock.accept()
        data = 'welcome to the echo server'    
        connection.sendall(data.encode("utf-8"))
        while True:
            data = connection.recv(1024)
            print('received "%s"' % data.decode("utf-8") )
            if data:
                connection.sendall(data.upper())
            else:
                break
    finally:
        connection.close()

