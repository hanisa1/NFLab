#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
###### Fill in start #######
serverPort = 6676 
serverSocket.bind(('', serverPort)) #binds the program to socket
serverSocket.listen(1) #Starts a new session
#Fill in end
while True: # while the server is up. proceed -> true 
    #Establish the connection
    print('Ready to serve...')
    #Fill in start ... 
    connectionSocket, addr = serverSocket.accept() #accepts input socket, starts connection
    #Fill in end
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket
        #Fill in start
        res = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(res.encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        # #Fill in end
        #Close client socket
        res2 = "HTTP/1.1 404 Not found\r\n\r\n"
        for i in range(0, len(res2)): 
            connectionSocket.send(res2[i].encode())
        connectionSocket.send(res2.encode())
        connectionSocket.close()
        
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data