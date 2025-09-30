try:
	from Pyside6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except :
	from Pyside2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__filr__),'icons'))

class PrimitiveCreatorDialog(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)

		self.resize(300,300)
		self.setWindowTitle(" 😒 Primitive Creator")

		self.main_layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.ob_listWidget = QtWidgets.QLisWidget()
		self.ob_listWidget.setIconSize(QtCore.QSize(60,60))
		self.ob_listWidget.setSpacing(5)
		self.ob_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.ob_listWidget.setMovement(QtWidgets.QListView.Static)
		self.ob_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.main_layout.addWidget(self.ob_listWidget)

		self.name_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addWidget(self.name_layout)
		self.name_label = QtWidgets.QLabel('Name : ')
		self.name_lineEdit = QtWidgets.QLineEdit()
		self.name_lineEdit.setStyleSheet(
			'''
				QLineEdit {
					border-radius : 5px;
					background-color : white;
					color : navy;
					font-size : 24px;
					font-family : Oswald;
				}
			'''
			)

		self.name_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_lineEdit)

		self.button_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)
		self.create_button = QtWidgets.QPushButton('💚 Create ')
		self.create_button.setStyleSheet(
			'''
				QPushButton {
					background-color : #ED378D
				}
			'''
		)

		self.cancel_button = QtWidgets.QPushButton('❤️ Cancel ')
		self.button_layout.addStretch()
		self.button_layout.addWidget(self.create_button)
		self.button_layout.addWidget(self.cancel_button)

		self.initIconWidget()

	def initIconWidget(self):
		objs = ['cube','cone','sphere','torus']
		for obj in objs:
			item = QtWidgets.QLisWidgetItem(obj)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH,f'{obj}.png')))
			self.ob_listWidget.addItem(item)

def run():
	global ui

	try:
		ui.close()
	except:
		pass
 
	ptr= wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.Qwidget)
	ui = PrimitiveCreatorDialog(parent=ptr)
	ui.show()