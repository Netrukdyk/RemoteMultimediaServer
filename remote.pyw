import sys
from PySide.QtUiTools import QUiLoader
from PySide.QtCore import *
from PySide.QtGui import *
from VirtMediaKeyb import * 
from TcpServer import *

class Gui(QApplication):

	def __init__(self, args):
		super(Gui, self).__init__(args)
		self.initUI()

	def initUI(self):
		loader = QUiLoader()
		self.ui = loader.load("remote.ui")
		self.ui.show()

		self.ui.prev.clicked.connect(self.onPrevPressed)
		self.ui.play.clicked.connect(self.onPlayPressed)
		self.ui.stop.clicked.connect(self.onStopPressed)
		self.ui.next.clicked.connect(self.onNextPressed)
		self.ui.vol_up.clicked.connect(self.onVol_upPressed)
		self.ui.vol_down.clicked.connect(self.onVol_downPressed)
		self.ui.mute.clicked.connect(self.onMutePressed)
		self.ui.media.clicked.connect(self.onMediaPressed)
		self.ui.zoom.clicked.connect(self.onZoomPressed)
		
		
		self.server = Server(7000)		
		self.ui.server_ip.setText(self.server.ip)
		self.server.message.connect(self.onServerMessage)
		
	def onServerMessage(self, msg):	
		msg = msg.rstrip()
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
			print(msg)

	def onPrevPressed(self):
		prev()		

	def onNextPressed(self):
		next()

	def onVol_upPressed(self):
		volu()

	def onVol_downPressed(self):
		vold()
		
	def onPlayPressed(self):
		play()
		
	def onStopPressed(self):
		stop()

	def onMutePressed(self):
		mute()
		
	def onMediaPressed(self):
		media()
		
	def onZoomPressed(self):
		zoom()
		

def main():
	ex = Gui(sys.argv)
	sys.exit(ex.exec_())


if __name__ == '__main__':
	main()
