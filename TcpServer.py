from PySide.QtCore import *
from PySide.QtNetwork import *
from LocalIp import getLocalIp

class Server(QTcpServer):
	message = Signal(str)
	
	def __init__(self, port):
		QTcpServer.__init__(self)		
		self.port = port		
		self.ip = getLocalIp()
		self.startUdp()
				
		self.listen(QHostAddress.Any, self.port)
		print("Listening on "+str(self.port))
		self.newConnection.connect(self.onNewClient)
		self.clients = []
	
#-------- UDP EVENTS----------	
	def startUdp(self):
		self.udp = QUdpSocket(self);
		self.udp.bind(self.port)
		self.udp.readyRead.connect(self.onUdpReadyRead)
		self.udp.waitForReadyRead(10)
	
	def onUdpReadyRead(self):
		udp = self.udp
		while udp.hasPendingDatagrams():
			datagram = QByteArray()
			datagram.resize(64)
			(datagram, sender, senderPort) = udp.readDatagram(64)
			data = QByteArray.fromBase64(datagram).split("_")
			(num, ok) = data[1].toInt(10)
			num = num + 1234
			QByteArray.number(num)
			
			if(data[0]=="RMS"):
				respond = QByteArray.toBase64(data[0]+"_"+QByteArray.number(num)+"#"+self.ip)
				udp.writeDatagram(respond, QHostAddress(sender), self.port)
			
			
			

#-------- SERVER EVENTS----------
	def onNewClient(self):
		sock = self.nextPendingConnection()
		client = Client(sock)
		self.clients.append(client)
		client.disconnected.connect(self.onClientDisconnected)
		client.command.connect(self.onClientCommand)

	def onClientDisconnected(self):
		client = self.sender()
		print("Client from "+client.socket.peerAddress().toString()+":"+str(client.socket.peerPort())+" disconnected")										
		self.clients.remove(client)
		
	def onClientCommand(self, value):
		self.message.emit(value)

class Client(QObject):
	disconnected = Signal()
	command = Signal(str)
	
	def __init__(self, socket):
		QObject.__init__(self)
		self.socket = socket
		self.socket.disconnected.connect(self.disconnected.emit)
		self.ip = socket.peerAddress().toString()
		self.port = str(socket.peerPort())
		print("New connection from "+self.ip+":"+self.port)
		self.handler = Handler(self)
	
class Handler(QObject):
	def __init__(self, client):
		self.client = client
		self.socket = client.socket
		self.socket.readyRead.connect(self.onReadyRead)
		self.client.socket.waitForReadyRead(10)
		
	def onReadyRead(self):
		print("Reading TCP")
		value = self.socket.readAll().data().decode("utf-8")
		self.client.command.emit(value)
