from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout
import sys
import numpy as np
import pyqtgraph as pg


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQtGraph Bar graph')

        hbox = QHBoxLayout()

        win = pg.PlotWidget()

        x = np.arange(10)
        y1 = np.sin(x)
        y2 = 1.1 * np.sin(x + 1)
        y3 = 1.2 * np.sin(x + 2)

        bar_1 = pg.BarGraphItem(x=x, height=y1, width=0.3, brush='r')
        bar_2 = pg.BarGraphItem(x=x+0.33, height=y2, width=0.3, brush='g')
        bar_3 = pg.BarGraphItem(x=x+0.66, height=y3, width=0.3, brush='b')

        win.addItem(bar_1)
        win.addItem(bar_2)
        win.addItem(bar_3)

        hbox.addWidget(win)
        self.setLayout(hbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
