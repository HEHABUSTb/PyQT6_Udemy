from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 100, 497, 420)
        self.setWindowTitle('PyQT6 GUI')
        self.setWindowIcon(QIcon('images/python.png'))
        # self.setFixedHeight(400)
        # self.setFixedWidth(700)
        # self.setStyleSheet('background-color:black')
        # self.setWindowOpacity(0.5)

        label = QLabel("Python GUI Development", self)
        label.setText('New text is Here')
        label.move(100, 100)
        label.setFont(QFont('Sanserif', 15))
        label.setStyleSheet('color:green')
        label.setNum(15)
        label.clear()

        """
        label2 = QLabel(self)
        pixmap = QPixmap('images/giphy.gif')
        label2.setPixmap(pixmap)
        """
        label3 = QLabel(self)
        movie = QMovie('images/giphy.gif')
        movie.setSpeed(100)
        label3.setMovie(movie)
        movie.start()




app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
