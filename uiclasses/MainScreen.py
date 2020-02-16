import os

from uiclasses.AttachmentBox import AttachmentBox
import time
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, uic
import pyscreenshot as ImageGrab

from tools.DataProvider import DataProvider


class MainScreen(QtWidgets.QMainWindow):
    path = os.path.expanduser("~") + r"\Documents\Redbutton"

    def __init__(self):

        super(MainScreen, self).__init__()
        im = ImageGrab.grab()
        im.save(self.path + r'\newproblem.png')
        dProvider = DataProvider()
        uic.loadUi('ui/redbutton.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'takeScreenShot')
        self.screenShotView = self.findChild(QtWidgets.QLabel, 'screenShotView')
        self.attachmentTab = self.findChild(QtWidgets.QWidget, 'tab_2')
        self.bsystemlist = self.findChild(QtWidgets.QComboBox, 'bssystemlist')
        self.priority = self.findChild(QtWidgets.QComboBox, 'priority')
        self.attachmentBox = AttachmentBox(self.attachmentTab)
        self.bsystemlist.addItems(dProvider.get_business_system())
        self.priority.addItems(dProvider.get_priority_list())
        self.button.clicked.connect(self.createScreenShot)
        self.attachmentBox.setAcceptDrops(True)
        pixmap = QPixmap(self.path + r'\newproblem.png').scaled(200, 160)
        self.screenShotView.setPixmap(pixmap)
        self.show()

    def createScreenShot(self):
        self.hide()
        time.sleep(0.5)
        im = ImageGrab.grab()
        im.save(self.path + r'\newproblem.png')
        pixmap = QPixmap(self.path + r'\newproblem.png').scaled(200, 160)
        self.screenShotView.setPixmap(pixmap)
        self.show()

