from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(418, 202)
        self.button_search = QtWidgets.QPushButton(Form)
        self.button_search.setGeometry(QtCore.QRect(310, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_search.setFont(font)
        self.button_search.setObjectName("button_search")
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setGeometry(QtCore.QRect(20, 150, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: green")
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(120, 10, 291, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_data_base_name = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_data_base_name.setFont(font)
        self.lineEdit_data_base_name.setObjectName("lineEdit_data_base_name")
        self.verticalLayout.addWidget(self.lineEdit_data_base_name)
        self.lineEdit_table_name = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_table_name.setFont(font)
        self.lineEdit_table_name.setObjectName("lineEdit_table_name")
        self.verticalLayout.addWidget(self.lineEdit_table_name)
        self.lineEdit_user_name = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_user_name.setFont(font)
        self.lineEdit_user_name.setObjectName("lineEdit_user_name")
        self.verticalLayout.addWidget(self.lineEdit_user_name)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(0, 20, 127, 111))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.button_search.clicked.connect(self.search_password)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_search.setText(_translate("Form", "search"))
        self.lineEdit_data_base_name.setText(_translate("Form", "first"))
        self.lineEdit_table_name.setText(_translate("Form", "users"))
        self.lineEdit_user_name.setText(_translate("Form", "enter user name"))
        self.label.setText(_translate("Form", "Data Base name:"))
        self.label_3.setText(_translate("Form", "     Table Name:"))
        self.label_2.setText(_translate("Form", "       User name:"))

    def search_password(self):
        try:
            database_name = self.lineEdit_data_base_name.text()
            table_name = self.lineEdit_table_name.text()
            user_name = self.lineEdit_user_name.text()
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database=database_name
            )

            cursor = mydb.cursor()
            cursor.execute(f"SELECT password FROM {table_name} WHERE user_name like '{user_name}'")

            row = cursor.fetchone()

            if row is None:
                self.label_result.setStyleSheet("color: red")
                self.label_result.setText(f'User {user_name} not found')
            else:
                self.label_result.setStyleSheet("color: green")
                self.label_result.setText(row[0])




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
