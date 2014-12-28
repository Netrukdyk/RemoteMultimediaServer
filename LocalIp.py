import socket

def getLocalIp():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	IP = socket.gethostbyname(socket.gethostname())
	s.close()
	return IP