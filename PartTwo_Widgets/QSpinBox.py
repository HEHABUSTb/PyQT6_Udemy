from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QHBoxLayout, QLabel, QSpinBox, QLineEdit
from PyQt6.QtGui import QIcon, QFont

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 497, 420)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(QIcon('images/python.png'))

        hbox = QHBoxLayout()
        self.label = QLabel('Laptop Price: ')
        self.label.setFont(QFont('Times', 14))
        self.line_edit = QLineEdit()
        self.line_edit.setText('0')
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spinbox_selected)
        self.total_result = QLineEdit()

        hbox.addWidget(self.label)
        hbox.addWidget(self.line_edit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.total_result)

        self.setLayout(hbox)

    def spinbox_selected(self):
        if self.line_edit.text() != '0':
            price = self.line_edit.text()

            total_price = int(price) * self.spinbox.value()
            self.total_result.setText(str(total_price))
        else:
            self.total_result.setText('Wrong value')





app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
