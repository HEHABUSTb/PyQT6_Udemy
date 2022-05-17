from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QListWidget
import sys
import numpy as np
import pyqtgraph as pg


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQtGraph Line graph')
        button = QPushButton('Click Me!')
        text = QLineEdit('Some Text')
        list_widget = QListWidget()

        grid = QGridLayout()

        my_plot = pg.PlotWidget()
        x = np.array([0, 3, 7, 4])
        y = np.array([5, 6, 7, 8])
        my_plot.plot(x, y)

        grid.addWidget(button, 0, 0)
        grid.addWidget(text, 1, 0)
        grid.addWidget(list_widget, 2, 0 )
        grid.addWidget(my_plot, 0, 1, 3, 1)

        self.setLayout(grid)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
