from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtSlot
from PyQt6.QtWidgets import QApplication
import sys


class Window(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot()
    def hello(self):
        print('hello')


app = QApplication(sys.argv)

engine = QQmlApplicationEngine()

window = Window()

engine.rootContext().setContextProperty('window', window)
engine.load('label.qml')
sys.exit(app.exec())

