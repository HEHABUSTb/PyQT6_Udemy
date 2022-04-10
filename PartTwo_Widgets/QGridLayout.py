from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 497, 420)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(QIcon('images/python.png'))

        grid = QGridLayout()

        buttons = []
        buttons.append(QPushButton('Click One'))
        buttons.append(QPushButton('Click Two'))
        buttons.append(QPushButton('Click Three'))
        buttons.append(QPushButton('Click Four'))
        buttons.append(QPushButton('Click Five'))
        buttons.append(QPushButton('Click Six'))
        buttons.append(QPushButton('Click Seven'))
        buttons.append(QPushButton('Click Eight'))

        row = 0
        column = 0

        for i in range(0, 8):
            print(i, row, column)
            grid.addWidget(buttons[i], row, column)
            column += 1
            if i == 3:
                column = 0
                row += 1


        self.setLayout(grid)




app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
