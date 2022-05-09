import sys
from PyQt6.QtWidgets import QApplication
from PartEight_Library.LibrarySystem import LibrarySystem

app = QApplication(sys.argv)
library = LibrarySystem()

sys.exit(app.exec())
