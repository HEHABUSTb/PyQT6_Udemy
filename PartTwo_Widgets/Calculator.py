# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(355, 218)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(16, 10, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_first = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_first.setFont(font)
        self.lineEdit_first.setObjectName("lineEdit_first")
        self.horizontalLayout.addWidget(self.lineEdit_first)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_second = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_second.setFont(font)
        self.lineEdit_second.setObjectName("lineEdit_second")
        self.horizontalLayout_2.addWidget(self.lineEdit_second)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_add = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_add.setFont(font)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout_3.addWidget(self.button_add)
        self.button_minus = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_minus.setFont(font)
        self.button_minus.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.button_minus)
        self.button_multiplier = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_multiplier.setFont(font)
        self.button_multiplier.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.button_multiplier)
        self.pushButton_division = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_division.setFont(font)
        self.pushButton_division.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_division)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_result.setStyleSheet("QLabel{\n"
"color:green\n"
"}\n"
"")
        self.label_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_result.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_result)

        self.button_add.clicked.connect(self.add)
        self.button_minus.clicked.connect(self.minus)
        self.button_multiplier.clicked.connect(self.multiplication)
        self.pushButton_division.clicked.connect(self.division)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add(self):
        first_number = int(self.lineEdit_first.text())
        second_number = int(self.lineEdit_second.text())
        result = first_number + second_number
        self.label_result.setText("Result = " + str(result))

    def minus(self):
        first_number = int(self.lineEdit_first.text())
        second_number = int(self.lineEdit_second.text())
        result = first_number - second_number
        self.label_result.setText("Result = " + str(result))

    def division(self):
        first_number = int(self.lineEdit_first.text())
        second_number = int(self.lineEdit_second.text())
        result = first_number / second_number
        self.label_result.setText("Result = " + str(result))

    def multiplication(self):
        first_number = int(self.lineEdit_first.text())
        second_number = int(self.lineEdit_second.text())
        result = first_number * second_number
        self.label_result.setText("Result = " + str(result))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "First Number"))
        self.lineEdit_first.setPlaceholderText(_translate("Form", "Please Enter number"))
        self.label_2.setText(_translate("Form", "Second Number"))
        self.lineEdit_second.setPlaceholderText(_translate("Form", "Please Enter number"))
        self.button_add.setText(_translate("Form", "+"))
        self.button_minus.setText(_translate("Form", "-"))
        self.button_multiplier.setText(_translate("Form", "*"))
        self.pushButton_division.setText(_translate("Form", "/"))
        self.label_result.setText(_translate("Form", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
