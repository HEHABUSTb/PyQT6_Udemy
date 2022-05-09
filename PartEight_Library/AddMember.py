from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Member_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_member_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_member_id.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_member_id.setFont(font)
        self.lineEdit_member_id.setObjectName("lineEdit_member_id")
        self.verticalLayout.addWidget(self.lineEdit_member_id)
        self.lineEdit_member_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_member_name.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_member_name.setFont(font)
        self.lineEdit_member_name.setObjectName("lineEdit_member_name")
        self.verticalLayout.addWidget(self.lineEdit_member_name)
        self.lineEdit_member_mobile = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_member_mobile.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_member_mobile.setFont(font)
        self.lineEdit_member_mobile.setObjectName("lineEdit_member_mobile")
        self.verticalLayout.addWidget(self.lineEdit_member_mobile)
        self.lineEdit_member_email = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_member_email.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_member_email.setFont(font)
        self.lineEdit_member_email.setObjectName("lineEdit_member_email")
        self.verticalLayout.addWidget(self.lineEdit_member_email)
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("QPushButton{\n"
"background-color:grey;\n"
"color:white\n"
"}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)
        self.label_result = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_save.clicked.connect(self.insert_member)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Insert Title"))
        self.lineEdit_member_id.setPlaceholderText(_translate("Dialog", "Please Enter Member ID"))
        self.lineEdit_member_name.setPlaceholderText(_translate("Dialog", "Please Enter Member Name"))
        self.lineEdit_member_mobile.setPlaceholderText(_translate("Dialog", "Please Enter Member Mobile"))
        self.lineEdit_member_email.setPlaceholderText(_translate("Dialog", "Please Enter Member email"))
        self.pushButton_save.setText(_translate("Dialog", "Insert Member"))

    def insert_member(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='library'
            )

            id = self.lineEdit_member_id.text()
            name = self.lineEdit_member_name.text()
            mobile = self.lineEdit_member_mobile.text()
            email = self.lineEdit_member_email.text()

            for text in (id, name, mobile, email):
                if text == '':
                    self.label_result.setText('Please add all fields')
                    self.label_result.setStyleSheet('color:red')
                    return

            cursor = mydb.cursor()
            querry = "INSERT INTO table_members (id, name, mobile, email) VALUES (%s, %s, %s, %s)"
            values = (id, name, mobile, email)
            cursor.execute(querry, values)

            mydb.commit()

            self.label_result.setText('Member added Successfully')
            self.label_result.setStyleSheet('color:green')

            self.lineEdit_member_email.setText('')
            self.lineEdit_member_id.setText('')
            self.lineEdit_member_name.setText('')
            self.lineEdit_member_mobile.setText('')

        except mc.Error as e:
            print(e)
            self.label_result.setText('Failed to add book')
            self.label_result.setStyleSheet('color:red')
