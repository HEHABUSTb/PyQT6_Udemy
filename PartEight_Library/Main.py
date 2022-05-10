import sys
import traceback

from PyQt6.QtWidgets import QApplication
from PartEight_Library.LibrarySystem import LibrarySystem


def error_handler(etype, value, tb):
    error_msg = ''.join(traceback.format_exception(etype, value, tb))
    raise error_msg

sys.excepthook = error_handler
app = QApplication(sys.argv)
library = LibrarySystem()

sys.exit(app.exec())
