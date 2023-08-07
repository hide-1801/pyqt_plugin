import sys
from PyQt5.Qt import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from pyqtplugins.lineeditwithlabel import *


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('ui/main.ui')

window.widget.setText('context')
window.widget.setTitle('title')

window.show()
app.exec()