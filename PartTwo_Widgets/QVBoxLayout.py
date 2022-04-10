from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 497, 420)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(QIcon('images/python.png'))

        vbox = QVBoxLayout()

        button_1 = QPushButton('Click One')
        button_2 = QPushButton('Click Two')
        button_3 = QPushButton('Click Three')
        button_4 = QPushButton('Click Four')

        vbox.addWidget(button_1)
        vbox.addWidget(button_2)
        vbox.addWidget(button_3)
        vbox.addWidget(button_4)
        vbox.addSpacing(100)
        vbox.addStretch(5)

        self.setLayout(vbox)




app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
