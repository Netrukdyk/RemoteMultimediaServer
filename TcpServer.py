from PySide.QtCore import *
from PySide.QtNetwork import *
from LocalIp import getLocalIp
from VirtMediaKeyb import * 

class Server(QTcpServer):
	onClientAdded = Signal()
	onClientRemoved = Signal()
	def __init__(self, port):
		QTcpServer.__init__(self)		
		self.port = port
		self.serverId = getLocalIp()
		self.ip = self.serverId[1]
		self.name = self.serverId[0]
		self.startUdp()
				
		self.listen(QHostAddress.Any, self.port)
		print("Listening TCP on "+str(self.port))
		self.newConnection.connect(self.onNewClient)
		self.clients = []
	
#-------- UDP EVENTS----------	
	def startUdp(self):
		self.udp = QUdpSocket(self);
		self.udp.bind(self.port)
		print("UDP bound on", self.port)
		self.udp.readyRead.connect(self.onUdpReadyRead)
		self.udp.waitForReadyRead(10)
	
	def onUdpReadyRead(self):
		udp = self.udp
		while udp.hasPendingDatagrams():
			datagram = QByteArray()
			datagram.resize(udp.pendingDatagramSize())
			(datagram, sender, senderPort) = udp.readDatagram(datagram.size())
			print(QByteArray.fromBase64(datagram))
			data = QByteArray.fromBase64(datagram).split("_")
			print("UDP:",data[0]+"_"+data[1])
			(num, ok) = data[1].toInt(10)			
			num = num + 1234
			QByteArray.number(num)
			
			if(data[0]=="RMS"):
				#RMS_0000#192.168.1.200#Mindis-PC
				respond = data[0]+"_"+QByteArray.number(num)+"#"+self.ip+"#"+self.name
				udp.writeDatagram(QByteArray.toBase64(respond), QHostAddress(sender), senderPort)

#-------- SERVER EVENTS----------
	def onNewClient(self):
		sock = self.nextPendingConnection()
		client = Client(sock)
		self.clients.append(client)
		client.disconnected.connect(self.onClientDisconnected)
		self.onClientAdded.emit()

	def onClientDisconnected(self):
		client = self.sender()
		print("Client from "+client.socket.peerAddress().toString()+":"+str(client.socket.peerPort())+" disconnected")										
		self.clients.remove(client)
		self.onClientRemoved.emit()

class Client(QObject):
	disconnected = Signal()
	
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
		msg = self.socket.readAll().data().decode("utf-8").rstrip()	
		if msg == 'PREV':
			prev()
		elif msg == 'NEXT':
			next()
		elif msg == 'PLAY':
			play()
		elif msg == 'VOLU':
			volu()
		elif msg == 'VOLD':
			vold()
		elif msg == 'MUTE':
			mute()
		elif msg == 'STOP':
			stop()
		elif msg == 'ZOOM':
			zoom()
		elif msg == 'MEDIA':
			media()
		elif msg == 'SLEEP':
			sleep()
		else:
			print("TCP:",msg)
