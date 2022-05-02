from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt6.QtWidgets import QLineEdit


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 227)
        self.lineEdit_table_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_table_name.setGeometry(QtCore.QRect(120, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_table_name.setFont(font)
        self.lineEdit_table_name.setObjectName("lineEdit_table_name")
        self.label_table_name = QtWidgets.QLabel(Form)
        self.label_table_name.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_table_name.setFont(font)
        self.label_table_name.setObjectName("label_table_name")
        self.button_create_table = QtWidgets.QPushButton(Form)
        self.button_create_table.setGeometry(QtCore.QRect(410, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_create_table.setFont(font)
        self.button_create_table.setObjectName("button_create_table")
        self.button_insert_data = QtWidgets.QPushButton(Form)
        self.button_insert_data.setGeometry(QtCore.QRect(420, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_insert_data.setFont(font)
        self.button_insert_data.setObjectName("button_insert_data")
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setGeometry(QtCore.QRect(10, 185, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 70, 391, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_user_name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_user_name.setFont(font)
        self.label_user_name.setObjectName("label_user_name")
        self.horizontalLayout.addWidget(self.label_user_name)
        self.lineEdit_user_name = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_user_name.setFont(font)
        self.lineEdit_user_name.setObjectName("lineEdit_user_name")
        self.horizontalLayout.addWidget(self.lineEdit_user_name)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 130, 541, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_password = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_2.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.checkbox_show_password = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkbox_show_password.setFont(font)
        self.checkbox_show_password.setObjectName("checkbox_show_password")
        self.horizontalLayout_2.addWidget(self.checkbox_show_password)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.actions()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_table_name.setText(_translate("Form", "Table name"))
        self.button_create_table.setText(_translate("Form", "Create Table"))
        self.button_insert_data.setText(_translate("Form", "Insert Data"))
        self.label_user_name.setText(_translate("Form", "User Name"))
        self.label_password.setText(_translate("Form", "Password"))
        self.checkbox_show_password.setText(_translate("Form", "Show Password"))

    def actions(self):
        self.button_create_table.clicked.connect(self.create_table)
        self.button_insert_data.clicked.connect(self.insert_data)
        self.checkbox_show_password.stateChanged.connect(self.show_password)

    def create_table(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='first'
            )

            cursor = mydb.cursor()
            table_name = self.lineEdit_table_name.text()
            querry="CREATE TABLE %s (id INT AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(255), password VARCHAR(255))"

            cursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(255), password VARCHAR(255))")
            self.label_result.setText(f'Data base {table_name} create')
        except mc.Error as e:
            self.label_result.setText("Creation of data base failed")

    def insert_data(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='first'
            )

            cursor = mydb.cursor()
            user_name = self.lineEdit_user_name.text()
            user_password = self.lineEdit_password.text()
            values = (user_name, user_password)

            querry = "INSERT INTO users (user_name, password) VALUES (%s, %s)"
            cursor.execute(querry, values)

            mydb.commit()
            self.label_result.setText('Data Inserted')

        except mc.Error as e:
            self.label_result.setText("Some error has occurred")



    def show_password(self):
        if self.checkbox_show_password.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
