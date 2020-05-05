import socket
class SERVER:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = None
        self.connect = None

    
    def promt(self):
        request = self.connect.recv(800)#.decode()
        return request


    def Response(self, option):
        message = ""
        while len(message) < 4 or message[-5:] != "\r\n.\r\n":
            self.connect.send("\r\n".encode())
            line = self.promt().decode()
            print(line)
            if line != "\r\n":
                line += "\r\n"
            message += line
        if option==1:
            message=message.lower()
            print("message=",message[:-5])
            self.connect.send(message[:-5].encode())
        elif option==2:
            message=message.upper()
            print("message=",message[:-5])
            self.connect.send(message[:-5].encode())
        elif option==3:
            message=message[:-5]
            print("message=",message)
            self.connect.send(message[::-1].encode())
                        
    def Menu(self, template):
        print(template.decode())
        if template.decode() == "LOWER":
            data="Send data who end with 'end of date' Sequence"
            self.connect.sendall(data.encode())
            self.Response(1)
        elif template.decode() == "UPPER":
            data="Send data who end with 'end of date' Sequence"
            self.connect.sendall(data.encode())
            self.Response(2)
        elif template.decode() == "REVERSE":
            data="Send data who end with 'end of date' Sequence"
            self.connect.sendall(data.encode())
            self.Response(3)
        elif template.decode() == "QUIT":
            self.connect.close()
            self.newConnections()           
        elif template.decode() == "HELP":
            data="""Command:
            LOWER-data will be send as lower characters
            UPPER-data will be send as upper characters
            REVERSE-data will be send reverse
            QUIT-end of connection"""
            self.connect.sendall(data.encode())
        else:
            data="Invalid input try HELP for command"
            self.connect.sendall(data.encode())


    def run(self):
        while True:
            data = self.promt()
            print("Adres " + str(self.address) + ": " + data.decode("utf-8"))
            print("test")
            self.Menu(data)

    #Wait for new connections
    def newConnections(self):
        print("waiting for newConnections")
        self.connect, self.address = self.socket.accept()
        print("New connection at adress " + str(self.address))

    def main(self):
        #Get host and port
        host = '127.0.0.1'
        port = int(input())
        #Create new server socket
        self.socket.bind((host, port))
        self.socket.listen(1)
        self.newConnections()
        self.run()
    

if __name__ == "__main__":    
    server=SERVER()
    server.main()
