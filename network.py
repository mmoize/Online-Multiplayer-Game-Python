import socket
import pickle




# class Network:
#     def __init__(self):
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.server = "192.168.0.77"
#         self.port = 5555
#         self.addr = (self.server, self.port)
#         self.p = self.connect()


#     def getP(self):
#         print("from server getP()", self.p)
#         return self.p
   

#     # def connect(self):
#     #     try:
#     #         self.client.connect(self.addr)
#     #         return self.client.recv(2048).decode()
#     #     except:
#     #         pass

#     def connect(self):
#         try:
#            self.client.connect(self.addr)
#            return self.client.recv(2048).decode()
#         except:
#             pass

    
#     def send(self, data):
#         try:
#             self.client.send(str.encode(data))
#             return pickle.loads(self.client.recv(2048))
#         except socket.error as e:
#             print(e)       


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.77"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            print("its client ", self.client.recv(2048).decode())
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)


