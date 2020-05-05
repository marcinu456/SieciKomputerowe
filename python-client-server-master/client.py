import socket
import sys

host = '127.0.0.1'
port = int(input())

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)
    
request='\r\n'
while True:

    message = input()
    if message=="":
        message='\r\n'
    sock.send(message.encode())
    request = sock.recv(800).decode()
    if request!='\r\n':
        print(request)
    if message=="QUIT":
        sock.close()
        break
