from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Add_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_title = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_title.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_title.setFont(font)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout.addWidget(self.lineEdit_title)
        self.lineEdit_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_id.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout.addWidget(self.lineEdit_id)
        self.lineEdit_author = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_author.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_author.setFont(font)
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.verticalLayout.addWidget(self.lineEdit_author)
        self.lineEdit_publisher = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_publisher.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_publisher.setFont(font)
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")
        self.verticalLayout.addWidget(self.lineEdit_publisher)
        self.pushButton_add_book = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_add_book.setFont(font)
        self.pushButton_add_book.setObjectName("pushButton_add_book")
        self.verticalLayout.addWidget(self.pushButton_add_book)
        self.label_result = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.actions()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Book"))
        self.lineEdit_title.setPlaceholderText(_translate("Dialog", "Please Enter Title"))
        self.lineEdit_id.setPlaceholderText(_translate("Dialog", "Please Enter ID"))
        self.lineEdit_author.setPlaceholderText(_translate("Dialog", "Please Enter Author"))
        self.lineEdit_publisher.setPlaceholderText(_translate("Dialog", "Please Enter Publisher"))
        self.pushButton_add_book.setText(_translate("Dialog", "Add Book"))

    def actions(self):
        self.pushButton_add_book.clicked.connect(self.insert_book)

    def insert_book(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='library'
            )

            title = self.lineEdit_title.text()
            id = self.lineEdit_id.text()
            author = self.lineEdit_author.text()
            publisher = self.lineEdit_publisher.text()

            for text in (title, id, author, publisher):
                if text == '':
                    self.label_result.setText('Please add all fields')
                    self.label_result.setStyleSheet('color:red')
                    return

            cursor = mydb.cursor()
            query = "INSERT INTO table_addbook (title, id, author, publisher) VALUES (%s, %s, %s, %s)"
            values = (title, id, author, publisher)
            cursor.execute(query, values)
            mydb.commit()

            self.label_result.setText('Data added')
            self.label_result.setStyleSheet('color:green')

            self.lineEdit_id.setText('')
            self.lineEdit_author.setText('')
            self.lineEdit_title.setText('')
            self.lineEdit_publisher.setText('')

        except mc.Error as e:
            print(e)
            self.label_result.setText('Failed to add book')
            self.label_result.setStyleSheet('color:red')


