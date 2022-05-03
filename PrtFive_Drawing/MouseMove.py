from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont, QCursor
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQT6 Mouse Track')
        self.setWindowIcon(QIcon('images/python.png'))
        self.setMouseTracking(True)

        hbox = QHBoxLayout()

        self.label = QLabel('Mouse Track')
        self.label.setFont(QFont('Times', 15))

        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def mouseMoveEvent(self, event):
        #x = self.x()
        #y = self.y()
        x = QCursor().pos().x()
        y = QCursor().pos().y()
        print(x, y)

        text = f'X: {x}, Y: {y}'

        self.label.setText(text)
        self.update()




app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())