from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQT6 GUI')
        self.setWindowIcon(QIcon('images/python.png'))
        # self.setFixedHeight(400)
        # self.setFixedWidth(700)

        self.setStyleSheet('background-color:black')
        self.setWindowOpacity(0.5)



app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
