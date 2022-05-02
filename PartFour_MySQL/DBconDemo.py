from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 146)
        self.db_create = QtWidgets.QPushButton(Form)
        self.db_create.setGeometry(QtCore.QRect(10, 90, 100, 30))
        self.db_create.setObjectName("db_create")
        self.db_connect_button = QtWidgets.QPushButton(Form)
        self.db_connect_button.setGeometry(QtCore.QRect(120, 90, 100, 30))
        self.db_connect_button.setObjectName("db_connect")
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setGeometry(QtCore.QRect(240, 80, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 30, 581, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.actions()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.db_create.setText(_translate("Form", "Create Databese"))
        self.db_connect_button.setText(_translate("Form", "Database connect"))
        self.label.setText(_translate("Form", "Database Name:"))

    def actions(self):
        self.db_create.clicked.connect(self.create_database)
        self.db_connect_button.clicked.connect(self.db_connect)

    def create_database(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password=''
            )

            cursor = mydb.cursor()
            dbname = self.lineEdit.text()

            cursor.execute(f"CREATE DATABASE {dbname}")
            self.label_result.setText(f'Data base {dbname} create')
        except mc.Error as e:
            self.label_result.setText("Creation of data base failed")

    def db_connect(self):
        try:
            db_name = self.lineEdit.text()
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database=db_name
            )
            self.label_result.setText('Connection was successful')
        except mc.Error as e:
            self.label_result.setText('Error in connection')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
