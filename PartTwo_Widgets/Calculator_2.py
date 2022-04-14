from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(332, 420)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setGeometry(QtCore.QRect(20, 10, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.button_minus = QtWidgets.QPushButton(Form)
        self.button_minus.setGeometry(QtCore.QRect(250, 210, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_minus.setFont(font)
        self.button_minus.setObjectName("button_minus")
        self.button_5 = QtWidgets.QPushButton(Form)
        self.button_5.setGeometry(QtCore.QRect(90, 210, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.button_3 = QtWidgets.QPushButton(Form)
        self.button_3.setGeometry(QtCore.QRect(170, 280, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.button_9 = QtWidgets.QPushButton(Form)
        self.button_9.setGeometry(QtCore.QRect(170, 140, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.button_0 = QtWidgets.QPushButton(Form)
        self.button_0.setGeometry(QtCore.QRect(90, 350, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.button_1 = QtWidgets.QPushButton(Form)
        self.button_1.setGeometry(QtCore.QRect(10, 280, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.button_8 = QtWidgets.QPushButton(Form)
        self.button_8.setGeometry(QtCore.QRect(90, 140, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.button_divide = QtWidgets.QPushButton(Form)
        self.button_divide.setGeometry(QtCore.QRect(250, 70, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_divide.setFont(font)
        self.button_divide.setObjectName("button_divide")
        self.button_equal = QtWidgets.QPushButton(Form)
        self.button_equal.setGeometry(QtCore.QRect(250, 350, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_equal.setFont(font)
        self.button_equal.setObjectName("button_equal")
        self.button_4 = QtWidgets.QPushButton(Form)
        self.button_4.setGeometry(QtCore.QRect(10, 210, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.button_clear = QtWidgets.QPushButton(Form)
        self.button_clear.setGeometry(QtCore.QRect(90, 70, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.button_comma = QtWidgets.QPushButton(Form)
        self.button_comma.setGeometry(QtCore.QRect(170, 350, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_comma.setFont(font)
        self.button_comma.setObjectName("button_comma")
        self.button_plus = QtWidgets.QPushButton(Form)
        self.button_plus.setGeometry(QtCore.QRect(250, 280, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_plus.setFont(font)
        self.button_plus.setObjectName("button_plus")
        self.button_delete = QtWidgets.QPushButton(Form)
        self.button_delete.setGeometry(QtCore.QRect(170, 70, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_delete.setFont(font)
        self.button_delete.setObjectName("button_delete")
        self.button_plus_and_minus = QtWidgets.QPushButton(Form)
        self.button_plus_and_minus.setGeometry(QtCore.QRect(10, 350, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_plus_and_minus.setFont(font)
        self.button_plus_and_minus.setText("")
        self.button_plus_and_minus.setObjectName("button_plus_and_minus")
        self.button_6 = QtWidgets.QPushButton(Form)
        self.button_6.setGeometry(QtCore.QRect(170, 210, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.button_degree = QtWidgets.QPushButton(Form)
        self.button_degree.setGeometry(QtCore.QRect(10, 70, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_degree.setFont(font)
        self.button_degree.setObjectName("button_degree")
        self.button_2 = QtWidgets.QPushButton(Form)
        self.button_2.setGeometry(QtCore.QRect(90, 280, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.button_7 = QtWidgets.QPushButton(Form)
        self.button_7.setGeometry(QtCore.QRect(10, 140, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.button_x = QtWidgets.QPushButton(Form)
        self.button_x.setGeometry(QtCore.QRect(250, 140, 75, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_x.setFont(font)
        self.button_x.setObjectName("button_x")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.add_functions()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.label_result.setText(_translate("Form", "0"))
        self.button_minus.setText(_translate("Form", "-"))
        self.button_5.setText(_translate("Form", "5"))
        self.button_3.setText(_translate("Form", "3"))
        self.button_9.setText(_translate("Form", "9"))
        self.button_0.setText(_translate("Form", "0"))
        self.button_1.setText(_translate("Form", "1"))
        self.button_8.setText(_translate("Form", "8"))
        self.button_divide.setText(_translate("Form", "/"))
        self.button_equal.setText(_translate("Form", "="))
        self.button_4.setText(_translate("Form", "4"))
        self.button_clear.setText(_translate("Form", "C"))
        self.button_comma.setText(_translate("Form", ","))
        self.button_plus.setText(_translate("Form", "+"))
        self.button_delete.setText(_translate("Form", "DEL"))
        self.button_6.setText(_translate("Form", "6"))
        self.button_degree.setText(_translate("Form", "X^2"))
        self.button_2.setText(_translate("Form", "2"))
        self.button_7.setText(_translate("Form", "7"))
        self.button_x.setText(_translate("Form", "X"))

    def add_functions(self):
        self.button_0.clicked.connect(lambda: self.write_number('0'))
        self.button_1.clicked.connect(lambda: self.write_number('1'))
        self.button_2.clicked.connect(lambda: self.write_number('2'))
        self.button_3.clicked.connect(lambda: self.write_number('3'))
        self.button_4.clicked.connect(lambda: self.write_number('4'))
        self.button_5.clicked.connect(lambda: self.write_number('5'))
        self.button_6.clicked.connect(lambda: self.write_number('6'))
        self.button_7.clicked.connect(lambda: self.write_number('7'))
        self.button_8.clicked.connect(lambda: self.write_number('8'))
        self.button_9.clicked.connect(lambda: self.write_number('9'))
        self.button_plus.clicked.connect(lambda: self.write_number('+'))
        self.button_minus.clicked.connect(lambda: self.write_number('-'))
        self.button_x.clicked.connect(lambda: self.write_number('*'))
        self.button_divide.clicked.connect(lambda: self.write_number('/'))

        self.button_clear.clicked.connect(self.clear)
        self.button_equal.clicked.connect(self.results)
        self.button_delete.clicked.connect(self.delete_number)
        self.button_comma.clicked.connect(self.add_comma)
        self.button_degree.clicked.connect(self.degree)

    def write_number(self, number: str):
        if self.label_result.text() == '0':
            self.label_result.setText(number)
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        result = eval(self.label_result.text())
        self.label_result.setText(str(result))

    def clear(self):
        self.label_result.setText('0')

    def delete_number(self):
        numbers = self.label_result.text()
        if numbers != '0':
            if len(numbers) == 1:
                self.label_result.setText('0')
            else:
                self.label_result.setText(numbers[:-1])

    def add_comma(self):
        numbers = self.label_result.text()
        if numbers[-1] != '.':
            self.label_result.setText(numbers + '.')

    def degree(self):
        numbers = self.label_result.text()
        self.label_result.setText(numbers + '**2')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
