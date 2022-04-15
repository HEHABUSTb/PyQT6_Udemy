from PyQt6.QtCore import QSize, QTime, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QLCDNumber
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('PyQT6 Radio button')
        self.setWindowIcon(QIcon('images/python.png'))

        timer = QTimer()
        timer.timeout.connect(self.showLCD)
        timer.start(1000)
        self.showLCD()

    def showLCD(self):
        vbox = QVBoxLayout()
        lcd = QLCDNumber()

        lcd.setStyleSheet('background:red')

        vbox.addWidget(lcd)

        time = QTime.currentTime()
        time_str = time.toString('hh:mm')

        lcd.display(time_str)

        self.setLayout(vbox)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
