import sys
from PySide.QtCore import *
from PySide.QtGui import *
import VirtMediaKeyb as kb
from TcpServer import *
from pyside_dynamic import *

class Ui(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		
		self.initTray()		
		loadUi('remote.ui', self)	
		
		self.prev.clicked.connect(kb.prev)
		self.play.clicked.connect(kb.play)
		self.stop.clicked.connect(kb.stop)
		self.next.clicked.connect(kb.next)
		self.vol_up.clicked.connect(kb.volu)
		self.vol_down.clicked.connect(kb.vold)
		self.mute.clicked.connect(kb.mute)
		self.media.clicked.connect(kb.media)
		self.zoom.clicked.connect(kb.zoom)				
		
	def initTray(self):
		self.m = QMenu()
		self.m.addAction(QApplication.style().standardIcon(QStyle.SP_DialogCloseButton), 'Exit', self.onTrayActionExit)		
		self.tray = QSystemTrayIcon(QIcon("icon.ico"), self)
		self.tray.activated.connect(self.onTrayActivated)		
		self.tray.setContextMenu(self.m)
		self.tray.show()
		
	def onTrayActivated(self, reason):
		if reason == QSystemTrayIcon.ActivationReason.Trigger:
			if self.isVisible():
				self.hide()
			else:
				self.show()
				self.setWindowState(Qt.WindowActive)
		
	def onTrayActionExit(self):
		self.m.destroy()
		self.m = None
		self.tray.hide()
		self.tray = None
		self.close()
			
	def changeEvent(self, event):
		if event.type() == QEvent.WindowStateChange:
			if self.windowState() & Qt.WindowMinimized:
				event.ignore()
				QTimer.singleShot(0, self.hide)
				#self.tray.showMessage('RemoteMultimedia', 'Running in the background.')
				return

class Remote(QObject):
	def __init__(self):
		self.app = QApplication(sys.argv)		
		self.server = Server(7000)		
		self.server.onClientAdded.connect(self.onClientConnected)
		self.server.onClientRemoved.connect(self.onClientDisconnected)
		self.ui = Ui()
		self.ui.show()
		self.ui.server_ip.setText(self.server.name+"@"+self.server.ip)
		
		self.recalculate()
		
		self.app.aboutToQuit.connect(self.exitHandler)
		sys.exit(self.app.exec_())
	
	def onClientConnected(self):
		self.recalculate()
	
	def onClientDisconnected(self):
		self.recalculate()

	def recalculate(self):
		self.ui.server_info.setTitle("Server info ("+str(len(self.server.clients))+" connected)")
		
	def exitHandler(self):
		self.server.close()
		self.server = None
		self.ui.close()
		self.ui = None
								
if __name__ == '__main__':
	Remote()
