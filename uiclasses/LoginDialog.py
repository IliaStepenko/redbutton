import os

from PyQt5 import QtGui, uic, QtWidgets

from tools.UserManager import UserManager
from uiclasses.MainScreen import MainScreen


class LoginDialog(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(LoginDialog,self).__init__(parent)

        uic.loadUi('ui/login_form.ui', self)

        self.username = self.findChild(QtWidgets.QLineEdit, 'username')
        self.password = self.findChild(QtWidgets.QLineEdit, 'password')


        self.login_btn = self.findChild(QtWidgets.QPushButton, 'login_btn')
        self.login_btn.clicked.connect(self.login_check)
        self.show()

    def login_check(self):

        user_manager = UserManager()

        if user_manager.authenticate(self.username.text(),self.password.text()) :
            self.close()
            self.cam = MainScreen()
            self.cam.show()
        else:
            print('apssword error')








