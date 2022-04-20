import os
import traceback
from PyQt6.QtGui import QFont, QTextCharFormat, QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QFontDialog, QColorDialog
from  PyQt6.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo, Qt
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

        self.actionBold.triggered.connect(self.set_bold)
        self.actionItalic.triggered.connect(self.set_italic)
        self.actionUnderline.triggered.connect(self.set_underline)

        self.actionCenter.triggered.connect(self.align_center)
        self.actionLeft.triggered.connect(self.align_left)
        self.actionRight.triggered.connect(self.align_right)
        self.actionJustify.triggered.connect(self.justify)

        self.actionFont.triggered.connect(self.font_dialog)
        self.actionColor.triggered.connect(self.color_dialog)
        self.actionAbout_App.triggered.connect(self.about_app)


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
            bold = True


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
        # font = QFont()
        # format = QTextCharFormat()
        # bold, italic, underline = self.check_formatting()
        format = self.textEdit.textCursor().charFormat()
        bold = format.font().bold()

        if bold is True:
            # print(self.textEdit.fontWeight())
            self.textEdit.setFontWeight(400)
        else:
            self.textEdit.setFontWeight(700)

            """Previous realisation"""
            # font.setBold(True)
            # format.setFont(font)
            # self.textEdit.textCursor().mergeCharFormat(format)

    def set_italic(self):
        format = self.textEdit.textCursor().charFormat()
        italic = format.font().italic()

        if italic is True:
            self.textEdit.setFontItalic(False)
        else:
            self.textEdit.setFontItalic(True)

    def set_underline(self):
        format = self.textEdit.textCursor().charFormat()
        italic = format.font().underline()

        if italic is True:
            self.textEdit.setFontUnderline(False)
        else:
            self.textEdit.setFontUnderline(True)

    def check_formatting(self):
        # assume no format by default
        bold = italic = underline = False

        format = self.textEdit.textCursor().charFormat()

        if format.font().bold() is True:
            bold = True
        if format.font().italic() is True:
            italic = True
        if format.font().underline() is True:
            underline = True

        return bold, italic, underline

    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def justify(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def font_dialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def about_app(self):
        QMessageBox.about(self, 'About App', 'This is my simple notepad')

def error_handler(etype, value, tb):
    error_msg = ''.join(traceback.format_exception(etype, value, tb))
    raise error_msg

sys.excepthook = error_handler
basedir = os.path.dirname(__file__)
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(basedir, "images", 'notepad.ico')))
Note = NotePadFunctions()
sys.exit(app.exec())