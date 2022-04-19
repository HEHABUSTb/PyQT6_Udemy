import traceback

from PyQt6.QtGui import QFont, QTextCharFormat
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from  PyQt6.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from  PyQt6.QtCore import QFileInfo
import sys
from NotePad import Ui_NotePadApp


class NotePadFunctions(QMainWindow, Ui_NotePadApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.actionSave.triggered.connect(self.save_file)
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPrint_Preview.triggered.connect(self.preview_dialog)
        self.actionExport_PDF.triggered.connect(self.export_pdf)
        self.actionQuit.triggered.connect(self.exit_app)

        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)

        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)

        self.actionBold.triggered.connect(self.set_bold_2)
        self.actionItalic.triggered.connect(self.set_bold_2)

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, "Save File")

        if filename[0]:
            file = open(filename[0], 'w')

            with file:
                text = self.textEdit.toPlainText()
                file.write(text)

                QMessageBox.about(self, 'Save', 'File has been saved')

    def maybe_save(self):
        if self.textEdit.document().isEmpty():
            return True

        question = QMessageBox.warning(self, 'Application',
                                       'The document has been modified. \n Do you want to save it?',
                                       QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)

        if question == QMessageBox.StandardButton.Save:
            return self.save_file()

        elif question == QMessageBox.StandardButton.Cancel:
            return False

        return True

    def new_file(self):
        if self.maybe_save():
            self.textEdit.clear()

    def open_file(self):
        filename = QFileDialog.getOpenFileNames(self, 'Open File', "")

        if filename[0]:
            file = open(filename[0], 'r')

            with file:
                data = file.read()
                self.textEdit.setText(data)

    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

    def preview_dialog(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.print_preview)
        preview_dialog.exec()

    def print_preview(self, printer):
        self.textEdit.print(printer)

    def export_pdf(self):
        file_name, suffix = QFileDialog.getSaveFileName(self, 'Export PDF', "PDF files (.pdf)")

        if file_name != '':
            if QFileInfo(file_name).suffix() == '': file_name += '.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(file_name)
            self.textEdit.document().print(printer)

    def exit_app(self):
        if self.maybe_save():
            self.close()

    def set_bold(self):
        font = QFont()
        font.setBold(True)
        #self.textEdit.setFont(font)
        text = self.textEdit.textCursor().selectedText()
        print(text.format())

        format = QTextCharFormat()
        format.setFont(font)
        self.textEdit.textCursor().mergeCharFormat(format)

    def set_bold_2(self):
        font = QFont()
        font.setBold(True)

        if self.check_formatting() is True:
            font.setBold(False)
            format = QTextCharFormat()
            format.setFont(font)
            self.textEdit.textCursor().mergeCharFormat(format)
        else:
            format = QTextCharFormat()
            format.setFont(font)
            self.textEdit.textCursor().mergeCharFormat(format)


    def check_formatting(self):
        # assume no format by default
        bold = italic = underline = False

        format = self.textEdit.textCursor().charFormat()

        if format.font().bold() is True:
            return True










def error_handler(etype, value, tb):
    error_msg = ''.join(traceback.format_exception(etype, value, tb))
    raise error_msg



sys.excepthook = error_handler
app = QApplication(sys.argv)
Note = NotePadFunctions()
sys.exit(app.exec())