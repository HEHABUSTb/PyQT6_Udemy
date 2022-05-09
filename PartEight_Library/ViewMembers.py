from PyQt6 import QtCore, QtGui, QtWidgets


class ViewMembers_Dialog(object):
    def setupUi(self, ViewMembers):
        ViewMembers.setObjectName("ViewMembers")
        ViewMembers.resize(650, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(ViewMembers)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(ViewMembers)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(157)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton_viewmembres = QtWidgets.QPushButton(ViewMembers)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_viewmembres.setFont(font)
        self.pushButton_viewmembres.setStyleSheet("QPushButton{\n"
"\n"
"background-color:rgb(218,218,218);\n"
"\n"
"\n"
"}")
        self.pushButton_viewmembres.setObjectName("pushButton_viewmembres")
        self.verticalLayout.addWidget(self.pushButton_viewmembres)

        self.retranslateUi(ViewMembers)
        QtCore.QMetaObject.connectSlotsByName(ViewMembers)

    def retranslateUi(self, ViewMembers):
        _translate = QtCore.QCoreApplication.translate
        ViewMembers.setWindowTitle(_translate("ViewMembers", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewMembers", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewMembers", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ViewMembers", "Mobile"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ViewMembers", "Email"))
        self.pushButton_viewmembres.setText(_translate("ViewMembers", "View Members"))
