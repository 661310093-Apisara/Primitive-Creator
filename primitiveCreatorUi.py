try:
	from Pyside6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except :
	from Pyside2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

class PrimitiveCreatorDialog(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)

		self.resize(300,300)
		self.setWindowTitle("Primitive Creator")

def run():
	global ui

	try:
		ui.close()
	except:
		pass

	ptr= wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.Qwidget)
	ui = PrimitiveCreatorDialog(parent=ptr)
	ui.show()