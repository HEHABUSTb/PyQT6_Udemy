from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('PyQT6 Radio button')
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_radio()




    def create_radio(self):
        hbox = QHBoxLayout()

        radio_1 = QRadioButton('Python')
        radio_1.setIcon(QIcon('images/py.png'))
        radio_1.setIconSize(QSize(30, 30))
        radio_1.setFont(QFont('Times', 14))
        radio_1.setChecked(True)
        radio_1.toggled.connect(self.radio_selected)

        radio_2 = QRadioButton('Java')
        radio_2.setIcon(QIcon('images/java.png'))
        radio_2.setIconSize(QSize(30, 30))
        radio_2.setFont(QFont('Times', 14))
        radio_2.toggled.connect(self.radio_selected)

        radio_3 = QRadioButton('Java Script')
        radio_3.setIcon(QIcon('images/javascript.png'))
        radio_3.setIconSize(QSize(30, 30))
        radio_3.setFont(QFont('Times', 14))
        radio_3.toggled.connect(self.radio_selected)

        hbox.addWidget(radio_1)
        hbox.addWidget(radio_2)
        hbox.addWidget(radio_3)

        self.label = QLabel('Hello')
        self.label.setFont(QFont('Sanserif', 15))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)


        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText(f'You have selected: {radio_btn.text()}')


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
