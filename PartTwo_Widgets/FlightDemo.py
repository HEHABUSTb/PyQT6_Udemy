# Form implementation generated from reading ui file 'FlightDemo.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(367, 313)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:yellow\n"
"}\n"
"QLabel{\n"
"color:green\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_first = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.radioButton_first.setFont(font)
        self.radioButton_first.setObjectName("radioButton_first")
        self.radioButton_first.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_first)
        self.radioButton_business = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.radioButton_business.setFont(font)
        self.radioButton_business.setObjectName("radioButton_business")
        self.radioButton_business.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_business)
        self.radioButton_economic = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.radioButton_economic.setFont(font)
        self.radioButton_economic.setObjectName("radioButton_economic")
        self.radioButton_economic.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_economic)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_result = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.verticalLayout_2.addWidget(self.label_result)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select flight Type"))
        self.radioButton_first.setText(_translate("Dialog", "First Class $150"))
        self.radioButton_business.setText(_translate("Dialog", "Business Class $120"))
        self.radioButton_economic.setText(_translate("Dialog", "Economic Class $100"))
        self.label_result.setText(_translate("Dialog", ""))

    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label_result.setText(f"You have selected: {radio_btn.text()}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
