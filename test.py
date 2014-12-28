import sys
from PySide import QtGui, QtCore
from pyside_dynamic import *

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		loadUi('remote.ui', self)

	def changeEvent(self, event):
		if event.type() == QtCore.QEvent.WindowStateChange:
			if self.windowState() & QtCore.Qt.WindowMinimized:
				event.ignore()
				print("Minimize")
				return


def main():
	app = QtGui.QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()