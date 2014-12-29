import socket

def getLocalIp():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 0))
	IP = s.getsockname()[0]
	NAME = socket.gethostname()
	s.close()
	return (NAME, IP)
	
	
if __name__ == '__main__':
	print(getLocalIp())