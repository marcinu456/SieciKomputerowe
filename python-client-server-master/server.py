import socket
#import threading


#Client class, new instance created for each connected client
#Each instance has the socket and address that is associated with items
#Along with an assigned ID and a name chosen by the client
class SERVER:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = None
        self.connect = None

    
    def promt(self):
        request = self.connect.recv(80)#.decode()
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
        # while True:
        #     #print(option)
        #     data=""
        #     print("data")
        #     endline=0
        #     while not endline:
        #         print("before")
        #         lump = self.socket.recv(1024)
        #         print("after")
        #         if len(lump):
        #             if len(data)>=2 and data[-2:] == '\r\n':
        #                 endline=1
        #                 data+=lump
        #                 client.socket.sendall(("testy").encode())
                        

    def Menu(self, template):
        print(template.decode())
        if template.decode() == "LOWER":
            self.Response(1)
        elif template.decode() == "UPPER":
            self.Response(2)
        elif template.decode() == "REVERSE":
            self.Response(3)
        elif template.decode() == "QUIT":
            self.connect.close()
            self.newConnections()           
        elif template.decode() == "HELP":
            data="to jest help"
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
