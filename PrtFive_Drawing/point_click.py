from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QPainter, QPen, QCursor
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQT6 Mouse Track')
        self.setWindowIcon(QIcon('images/python.png'))

        self.pos1 = [0, 0]

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        pen = QPen(Qt.GlobalColor.red, 15)
        painter.setPen(pen)
        painter.drawPoint(self.pos1[0], self.pos1[1])

    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            position = self.mapFromGlobal(QCursor.pos())
            print(position)
            self.pos1[0], self.pos1[1] = position.x(), position.y()
            self.update()

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())