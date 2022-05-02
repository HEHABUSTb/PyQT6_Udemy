from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt6.QtWidgets import QLineEdit, QDialog


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(425, 155)
        self.checkBox_show = QtWidgets.QCheckBox(Form)
        self.checkBox_show.setGeometry(QtCore.QRect(310, 60, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_show.setFont(font)
        self.checkBox_show.setObjectName("checkBox_show")
        self.button_login = QtWidgets.QPushButton(Form)
        self.button_login.setGeometry(QtCore.QRect(310, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setGeometry(QtCore.QRect(20, 90, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 276, 62))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_user_name = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_user_name.setFont(font)
        self.lineEdit_user_name.setText("")
        self.lineEdit_user_name.setObjectName("lineEdit_user_name")
        self.horizontalLayout.addWidget(self.lineEdit_user_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.actions()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox_show.setText(_translate("Form", "Show"))
        self.button_login.setText(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "User Name:"))
        self.label_2.setText(_translate("Form", " Password:"))

    def actions(self):
        self.checkBox_show.stateChanged.connect(self.show_password)
        self.button_login.clicked.connect(self.login)

    def show_password(self):
        if self.checkBox_show.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

    def login(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='first'
            )

            cursor = mydb.cursor()
            user_name = self.lineEdit_user_name.text()
            password = self.lineEdit_password.text()

            query = f"SELECT user_name, password FROM users WHERE user_name like '{user_name}' and password like '{password}'"
            cursor.execute(query)

            result = cursor.fetchone()

            if result is None:
                self.label_result.setStyleSheet("color: red")
                self.label_result.setText('Incorrect user name or password')
            else:
                self.label_result.setStyleSheet("color: green")
                self.label_result.setText('You are logged in')
                mydialog = QDialog()
                mydialog.setModal(True)
                mydialog.exec()


        except mc.Error as e:
            self.label_result.setStyleSheet("color: red")
            self.label_result.setText("Some error occurred")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
