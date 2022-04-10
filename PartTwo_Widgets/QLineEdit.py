from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 497, 420)
        self.setWindowTitle('QLine Edit')
        self.setWindowIcon(QIcon('images/python.png'))

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont('Sanserif', 15))
        #line_edit.setText('Enter text')
        line_edit.setPlaceholderText('Enter path')
        #line_edit.setEnabled(False)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)



app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
