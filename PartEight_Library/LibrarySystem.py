from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from MainGUI import Ui_MainWindow
from AddBook import Add_Dialog
from AddMember import Member_Dialog
from ViewBooks import View_Dialog
from ViewMembers import ViewMembers_Dialog
import mysql.connector as mc


class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_add_book.clicked.connect(self.add_book)
        self.toolButton_add_member.clicked.connect(self.add_member)
        self.toolButton_view_books.clicked.connect(self.view_books)
        self.toolButton_view_memers.clicked.connect(self.view_members)
        self.toolButton_submit_book.clicked.connect(self.submit_book)
        self.toolButton_renew.clicked.connect(self.renew_book)

        self.lineEdit_book_id.returnPressed.connect(self.book_id)
        self.lineEdit_member_id.returnPressed.connect(self.member_id)
        self.lineEdit_submission.returnPressed.connect(self.load_issue)

        self.toolButton_issue.clicked.connect(self.issue_book)

        self.config = {
            "host": 'localhost',
            "user": 'root',
            "password": '',
            "database": 'library'
        }

    def add_book(self):
        dialog = QDialog()
        ui = Add_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def add_member(self):
        dialog = QDialog()
        ui = Member_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def view_books(self):
        dialog = QDialog()
        ui = View_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def view_members(self):
        dialog = QDialog()
        ui = ViewMembers_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def book_id(self):
        id = self.lineEdit_book_id.text()

        try:
            mydb = mc.connect(**self.config)
            cursor = mydb.cursor()
            print(cursor)

            query = f"SELECT * FROM table_addbook WHERE id = '{id}'"
            print(query)
            cursor.execute(query)

            result = cursor.fetchall()
            for row in result:
                print(row)
                self.label_book_name.setText('Book Name: ' + row[0])
                self.label_book_author.setText('Book author: ' + row[2])

        except mc.Error as e:
            print(e)

    def member_id(self):
        id = self.lineEdit_member_id.text()

        try:
            mydb = mc.connect(**self.config)

            cursor = mydb.cursor()
            print(cursor)
            query = f"SELECT * FROM table_members WHERE id = '{id}'"
            print(query)
            cursor.execute(query)

            result = cursor.fetchall()
            for row in result:
                print(row)
                self.label_meber_name.setText("Member Name: " + row[1])
                self.label_contact_info.setText("Email: " + row[3])

        except mc.Error as e:
            print(e)

    def issue_book(self):
        book_id = self.lineEdit_book_id.text()
        member_id = self.lineEdit_member_id.text()

        try:
            mydb = mc.connect(**self.config)

            cursor = mydb.cursor()
            query_insert = f"INSERT INTO table_issue (book_id, member_id) VALUES ('{book_id}', '{member_id}')"
            query_available = f"UPDATE table_addbook SET isAvailable = FALSE WHERE id = '{book_id}'"

            cursor.execute(query_insert)
            cursor.execute(query_available)
            mydb.commit()

            QMessageBox.about(self, 'Issue Book', 'Book Issued')


        except mc.Error as e:
            print(e)


    def load_issue(self):
        issue_id = self.lineEdit_submission.text()

        try:
            mydb = mc.connect(**self.config)

            cursor = mydb.cursor()
            cursor.execute(f"SELECT * FROM table_issue WHERE book_id = '{issue_id}'")
            result = cursor.fetchall()

            self.tableWidget_book_info.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget_book_info.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget_book_info.setItem(row_number, column_number, QTableWidgetItem(str(data)))



        except mc.Error as e:
            print(e)

    def submit_book(self):
        book_id = self.lineEdit_submission.text()

        try:
            mydb = mc.connect(**self.config)

            if book_id == "":
                QMessageBox.about(self, 'Book Submission', 'Please choose a book')
                return

            cursor = mydb.cursor()
            query_delete = f"DELETE FROM table_issue WHERE book_id = '{book_id}'"
            query_update = f"UPDATE table_addbook SET isAvailable = True WHERE id = '{book_id}'"

            cursor.execute(query_delete)
            cursor.execute(query_update)
            mydb.commit()

            QMessageBox.about(self, "Book Submission", 'Book submitted')

        except mc.Error as e:
            print(e)

    def renew_book(self):
        book_id = self.lineEdit_submission.text()
        try:
            mydb = mc.connect(**self.config)

            if book_id == "":
                QMessageBox.about(self, 'Book Renew', 'Please choose a book')
                return

            cursor = mydb.cursor()
            query_update = f"UPDATE table_issue SET issue_time = CURRENT_TIMESTAMP, renew_count = renew_count + 1 WHERE book_id = '{book_id}'"
            cursor.execute(query_update)
            mydb.commit()

            QMessageBox.about(self, "Book Renew", 'Book renewed Successfully')

        except mc.Error as e:
            print(e)

