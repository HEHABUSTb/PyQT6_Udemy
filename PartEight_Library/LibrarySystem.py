from PyQt6.QtWidgets import QMainWindow, QDialog
from MainGUI import Ui_MainWindow
from AddBook import Add_Dialog
from AddMember import Member_Dialog
from ViewBooks import View_Dialog
from ViewMembers import ViewMembers_Dialog


class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_add_book.clicked.connect(self.add_book)
        self.toolButton_add_member.clicked.connect(self.add_member)
        self.toolButton_view_books.clicked.connect(self.view_books)
        self.toolButton_view_memers.clicked.connect(self.view_members)

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
