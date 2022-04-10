from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 497, 420)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(QIcon('images/python.png'))
        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton('Change Text')
        btn.clicked.connect(self.clicked_button)
        self.label = QLabel('Default text')

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_button(self):
        self.label.setText('Another Text')
        self.setFont(QFont('Times', 15))
        self.label.setStyleSheet('color:red')


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
