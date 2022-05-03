from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QCursor
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQT6 Mouse Track')
        self.setWindowIcon(QIcon('images/python.png'))
        self.setMouseTracking(True)

        vbox = QVBoxLayout()

        self.label_press = QLabel('Mouse Press')
        self.label_press.setFont(QFont('Times', 15))

        self.label_release = QLabel('Mouse Release')
        self.label_release.setFont(QFont('Times', 15))

        vbox.addWidget(self.label_press)
        vbox.addWidget(self.label_release)

        self.setLayout(vbox)


    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            x = self.x()
            y = self.y()

            text = f'X: {x}, Y: {y}'
            self.label_press.setText(text)

    def mouseReleaseEvent(self, event):
        x = self.x()
        y = self.y()

        text = f'X: {x}, Y: {y}'
        self.label_release.setText(text)
        self.update()


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())