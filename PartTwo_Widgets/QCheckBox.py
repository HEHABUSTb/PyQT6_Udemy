from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QCheckBox
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('PyQT6 Radio button')
        self.setWindowIcon(QIcon('images/python.png'))

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.checkbox = QCheckBox('Python')
        self.checkbox.setIcon(QIcon("images/py.png"))
        self.checkbox.setIconSize(QSize(30, 30))
        self.checkbox.setFont(QFont('Segoe print', 14))
        self.checkbox.stateChanged.connect(self.item_selected)

        self.checkbox_2 = QCheckBox('Java')
        self.checkbox_2.setIcon(QIcon("images/java.png"))
        self.checkbox_2.setIconSize(QSize(30, 30))
        self.checkbox_2.setFont(QFont('Segoe print', 14))
        self.checkbox_2.stateChanged.connect(self.item_selected)

        self.checkbox_3 = QCheckBox('Java Script')
        self.checkbox_3.setIcon(QIcon("images/javascript.png"))
        self.checkbox_3.setIconSize(QSize(30, 30))
        self.checkbox_3.setFont(QFont('Segoe print', 14))
        self.checkbox_3.stateChanged.connect(self.item_selected)

        self.label = QLabel('Hello')
        self.label.setFont(QFont('Segoe print', 14))

        hbox.addWidget(self.checkbox)
        hbox.addWidget(self.checkbox_2)
        hbox.addWidget(self.checkbox_3)

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)



    def item_selected(self):
        value = ''

        if self.checkbox.isChecked():
            value = self.checkbox.text()
        elif self.checkbox_2.isChecked():
            value = self.checkbox_2.text()
        elif self.checkbox_3.isChecked():
            value = self.checkbox_3.text()

        self.label.setText(value)







app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())