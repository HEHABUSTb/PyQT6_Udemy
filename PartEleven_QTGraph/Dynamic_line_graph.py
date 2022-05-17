from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QHBoxLayout
import sys
import numpy as np
import pyqtgraph as pg


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQtGraph Dynamic Line Graph')

        hbox_1 = QHBoxLayout()
        hbox_2 = QHBoxLayout()
        vbox = QVBoxLayout()

        self.x1 = QLineEdit()
        self.x2 = QLineEdit()
        self.x3 = QLineEdit()
        self.x4 = QLineEdit()

        self.y1 = QLineEdit()
        self.y2 = QLineEdit()
        self.y3 = QLineEdit()
        self.y4 = QLineEdit()

        button_plot = QPushButton('Plot')
        button_plot.clicked.connect(self.plot_graph)
        button_clear = QPushButton('Clear')
        button_clear.clicked.connect(self.clear_graph)

        self.my_plot = pg.PlotWidget()

        hbox_1.addWidget(self.x1)
        hbox_1.addWidget(self.x2)
        hbox_1.addWidget(self.x3)
        hbox_1.addWidget(self.x4)

        hbox_2.addWidget(self.y1)
        hbox_2.addWidget(self.y2)
        hbox_2.addWidget(self.y3)
        hbox_2.addWidget(self.y4)

        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addWidget(self.my_plot)
        vbox.addWidget(button_plot)
        vbox.addWidget(button_clear)

        self.setLayout(vbox)

    def plot_graph(self):
        x1 = int(self.x1.text())
        x2 = int(self.x2.text())
        x3 = int(self.x3.text())
        x4 = int(self.x4.text())

        y1 = int(self.y1.text())
        y2 = int(self.y2.text())
        y3 = int(self.y3.text())
        y4 = int(self.y4.text())

        x = np.array([x1, x2, x3, x4])
        y = np.array([y1, y2, y3, y4])

        self.my_plot.plot(x, y)

    def clear_graph(self):
        self.my_plot.clear()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
