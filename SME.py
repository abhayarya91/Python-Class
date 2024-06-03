# import socket
# serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = socket.gethostbyname()
# port = 9090
# serversocket.bind((host,port))
# serversocket.listen(5)

# while True:
#     clientsocket,addr= serversocket.accept()
#     print("connection initiated from %s" %str(addr))
#     msg ='connection Estevlished'+"\r\n"
#     clientsocket.send(msg.encode('ascii'))
#     clientsocket.close()



import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname('')
port = 9090
serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    print("Connection initiated from %s" % str(addr))
    msg = 'Connection established' + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
