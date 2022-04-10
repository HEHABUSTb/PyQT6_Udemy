from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 497, 420)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(QIcon('images/python.png'))

        hbox = QHBoxLayout()

        button_1 = QPushButton('Click One')
        button_2 = QPushButton('Click Two')
        button_3 = QPushButton('Click Three')
        button_4 = QPushButton('Click Four')

        hbox.addWidget(button_1)
        hbox.addWidget(button_2)
        hbox.addWidget(button_3)
        hbox.addWidget(button_4)
        hbox.addSpacing(100)
        hbox.addStretch(5)

        self.setLayout(hbox)



app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
