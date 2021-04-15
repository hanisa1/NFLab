from socket import *
serverName = '172.19.112.74'
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(( '', 5432))
message = input('Input lowercase sentence:') 
clientSocket.sendto(message.encode(),(serverName, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
print(modifiedMessage.decode()) 
clientSocket.close()