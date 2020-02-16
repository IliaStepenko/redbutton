import os

from PyQt5 import QtWidgets
import sys

from uiclasses.LoginDialog import LoginDialog
from uiclasses.MainScreen import MainScreen

app = QtWidgets.QApplication(sys.argv)

path = os.path.expanduser("~") + '\Documents\Redbutton'
try:
    file = open(path + "\Temp", "r")
    auth_token = file.read()
    if auth_token.find('Token') == -1:
        window = LoginDialog()
    else:
        window = MainScreen()
except:
    file = open(path + "\Temp", "w")
    window = LoginDialog()


app.exec_()