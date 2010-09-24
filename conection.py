import socket

class conection:
    """This module attempts to be the wrapper for all types of conections."""
    def __init__(self,message):
        self.port=10600
        self.broadcast="255.255.255.255"
        self.ip="localhost"
        self.message=message

    def udp(self):
        broadcast=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        broadcast.sendto(self.message,(self.broadcast,self.port))

    def tcp(self):
        tcp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        tcp.connect((self.ip,self.port))
        tcp.send(self.message)
        tcp.close()

#socketUDP=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#socketUDP.connect(("225.255.255.255",10600))
#socketUDP.setsockopt(socket.SO_BROADCAST, option, "v2/10/1/PING/6672100343/Homer")
#socketUDP.send("v2/10/1/PING/6672100343/Homer")
#socketUDP.close()




#host = '255.255.255.255'                               # Bind to all interfaces
#port = 10600
#
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#s.bind((host, port))
#address=(host,port)
## Acknowledge it.
#s.sendto("v2/10/1/PING/6672100343/Homer", address)
