from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QListWidget, QVBoxLayout
import sys
import numpy as np
import pyqtgraph as pg


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQtGraph Scatter')

        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)

        self.plot_widget = pg.PlotWidget()
        self.plot_widget.addLegend()  # Add Legend name
        self.plot = self.plot_widget.plot(x, y, pen=None, symbol='o', symbolBrush='b', name='Plot Name')


        self.button_plot = QPushButton('Replot')
        self.button_plot.clicked.connect(self.replot)

        vbox =QVBoxLayout()
        vbox.addWidget(self.plot_widget)
        vbox.addWidget(self.button_plot)

        self.setLayout(vbox)

    def replot(self):
        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        self.plot.setData(x, y)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
