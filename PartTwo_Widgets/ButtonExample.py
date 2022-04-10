from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 497, 420)
        self.setWindowTitle('PyQT6 GUI')
        self.setWindowIcon(QIcon('images/python.png'))
        # self.setFixedHeight(400)
        # self.setFixedWidth(700)
        # self.setStyleSheet('background-color:black')
        # self.setWindowOpacity(0.5)

        self.create_button('Click')

    def create_button(self, text: str):
        button = QPushButton(text, self)
        button.setGeometry(100, 100, 130, 130)
        button.setFont(QFont('Times', 14, QFont.Weight.Bold))
        button.setIcon(QIcon('images/python.png'))
        button.setIconSize(QSize(36,36))

        # popup menu
        menu = QMenu()
        menu.setFont(QFont('Times', 11, QFont.Weight.Bold))
        # menu.setStyleSheet('background-color:black')
        # menu.setStyleSheet('color:white')
        menu.addAction('Copy')
        menu.addAction('Cut')
        menu.addAction('Paste')

        button.setMenu(menu)




app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())