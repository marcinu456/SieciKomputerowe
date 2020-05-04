import socket
import sys

#Get host and port
host = '127.0.0.1'
port = int(input())

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)


#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network
request='\r\n'
while True:

    message = input()
    if message=="":
        message='\r\n'
    sock.send(message.encode())
    request = sock.recv(80).decode()
    if request!='\r\n':
        print(request)
    if message=="QUIT":
        sock.close()
        break
