from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QHBoxLayout, QLabel, QSpinBox, QLineEdit, \
    QDialog, QDoubleSpinBox
from PyQt6.QtGui import QIcon, QFont
from  PyQt6 import uic
import sys


class UI(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi("SpinDemo.ui", self)
        self.line_edit_price = self.findChild(QLineEdit, 'lineEdit_price')
        self.line_edit_price.setText('0')
        self.double_spin = self.findChild(QDoubleSpinBox, 'doubleSpinBox')
        self.double_spin.valueChanged.connect(self.spinbox_selected)
        self.line_edit_result = self.findChild(QLineEdit, 'lineEdit_result')

    def spinbox_selected(self):
        if self.line_edit_price.text() != '0':
            price = int(self.line_edit_price.text())
            total = price * self.double_spin.value()

            self.line_edit_result.setText(str(total))
        else:
            self.line_edit_result.setText('Wrong Value')


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
