from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QListWidget, QVBoxLayout
import sys
import numpy as np
import pyqtgraph as pg


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQtGraph Update graph')

        vbox = QVBoxLayout()

        self.plot_widget = pg.PlotWidget()
        self.button_update = QPushButton('Update')
        self.button_update.clicked.connect(self.show_plot)

        x = np.random.normal(size=100)
        y = np.random.normal(size=100)

        self.plot_widget.plot(x, y, clea=True)

        vbox.addWidget(self.plot_widget)
        vbox.addWidget(self.button_update)

        self.setLayout(vbox)

    def update(self):
        x = np.random.normal(size=100)
        y = np.random.normal(size=100)
        self.plot_widget.plot(x, y, clea=True)

    def show_plot(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
