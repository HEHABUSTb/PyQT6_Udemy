from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt6.QtWidgets import QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(568, 483)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_data_base = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_data_base.setFont(font)
        self.label_data_base.setObjectName("label_data_base")
        self.horizontalLayout.addWidget(self.label_data_base)
        self.lineEdit_data_base_name = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_data_base_name.setFont(font)
        self.lineEdit_data_base_name.setObjectName("lineEdit_data_base_name")
        self.horizontalLayout.addWidget(self.lineEdit_data_base_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_table_name = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_table_name.setFont(font)
        self.label_table_name.setObjectName("label_table_name")
        self.horizontalLayout_2.addWidget(self.label_table_name)
        self.lineEdit_table_name = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_table_name.setFont(font)
        self.lineEdit_table_name.setObjectName("lineEdit_table_name")
        self.horizontalLayout_2.addWidget(self.lineEdit_table_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.verticalLayout.addWidget(self.tableWidget)
        self.button_show_data = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_show_data.setFont(font)
        self.button_show_data.setObjectName("button_show_data")
        self.button_show_data.clicked.connect(self.show_data)
        self.verticalLayout.addWidget(self.button_show_data)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_data_base.setText(_translate("Form", "Database Name:"))
        self.lineEdit_data_base_name.setText(_translate("Form", "first"))
        self.label_table_name.setText(_translate("Form", "Table Name:"))
        self.lineEdit_table_name.setText(_translate("Form", "users"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "User Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Password"))
        self.button_show_data.setText(_translate("Form", "Show Data"))

    def show_data(self):
        try:
            database_name = self.lineEdit_data_base_name.text()
            table_name = self.lineEdit_table_name.text()
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database=database_name
            )

            cursor = mydb.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")

            result = cursor.fetchall()
            print(result)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
