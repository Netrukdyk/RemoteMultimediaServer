import sys
from PySide.QtUiTools import QUiLoader
from PySide.QtCore import *
from PySide.QtGui import *
from VirtMediaKeyb import * 
from TcpServer import *

class Remote(QApplication):

	def __init__(self, args):
		super(Remote, self).__init__(args)
		self.server = Server(7000)
		self.initUI()
		self.initTray()
		
	def initUI(self):
		loader = QUiLoader()
		self.ui = loader.load("remote.ui")
		self.ui.show()
		self.ui.server_ip.setText(self.server.ip)
		
		self.ui.prev.clicked.connect(prev)
		self.ui.play.clicked.connect(play)
		self.ui.stop.clicked.connect(stop)
		self.ui.next.clicked.connect(next)
		self.ui.vol_up.clicked.connect(volu)
		self.ui.vol_down.clicked.connect(vold)
		self.ui.mute.clicked.connect(mute)
		self.ui.media.clicked.connect(media)
		self.ui.zoom.clicked.connect(zoom)
	
	def initTray(self):
		self.tray = QSystemTrayIcon(QIcon("images/icon.ico"), self)
		self.m = QMenu()
		self.m.addAction('First')
		self.m.addAction('Second')
		self.tray.setContextMenu(self.m)
		self.tray.show()			

def main():
	rm = Remote(sys.argv)
	sys.exit(rm.exec_())

if __name__ == '__main__':
	main()
