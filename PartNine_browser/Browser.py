import traceback
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QLineEdit
from PyQt6.QtCore import Qt, QUrl, QSize
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWebEngineWidgets import QWebEngineView

import sys
import os


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 1024, 768)
        self.basedir = os.path.dirname(__file__)
        self.setWindowTitle('Simple Browser')
        self.setWindowIcon(QIcon(os.path.join(self.basedir, "images", 'python.png')))

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.back_button = QPushButton()
        self.back_button.setIcon(QIcon(os.path.join(self.basedir, "images", 'back.png')))
        self.back_button.setIconSize(QSize(36, 36))
        self.back_button.clicked.connect(self.back)
        toolbar.addWidget(self.back_button)

        self.reload_button = QPushButton()
        self.reload_button.setIcon(QIcon(os.path.join(self.basedir, "images", 'reload.png')))
        self.reload_button.setIconSize(QSize(36, 36))
        self.reload_button.clicked.connect(self.reload)
        toolbar.addWidget(self.reload_button)

        self.forward_button = QPushButton()
        self.forward_button.setIcon(QIcon(os.path.join(self.basedir, "images", 'forward.png')))
        self.forward_button.setIconSize(QSize(36, 36))
        self.forward_button.clicked.connect(self.forward)
        toolbar.addWidget(self.forward_button)

        self.home_button = QPushButton()
        self.home_button.setIcon(QIcon(os.path.join(self.basedir, "images", 'home.png')))
        self.home_button.setIconSize(QSize(36, 36))
        self.home_button.clicked.connect(self.home)
        toolbar.addWidget(self.home_button)

        self.line_edit = QLineEdit()
        self.line_edit.setFont(QFont('Times', 18))
        self.line_edit.returnPressed.connect(self.search)
        toolbar.addWidget(self.line_edit)

        self.search_button = QPushButton()
        self.search_button.setIcon(QIcon(os.path.join(self.basedir, "images", 'search.png')))
        self.search_button.setIconSize(QSize(36, 36))
        self.search_button.clicked.connect(self.search)
        toolbar.addWidget(self.search_button)

        self.web_engine_view = QWebEngineView()
        self.setCentralWidget(self.web_engine_view)

        self.initial_url = 'https://www.google.com'
        self.line_edit.setText('google.com')
        self.web_engine_view.load(QUrl(self.initial_url))

    def search(self):
        url = self.line_edit.text()
        if 'https://' not in url:
            url = 'https://' + url
        self.web_engine_view.load(QUrl(url))

    def back(self):
        self.web_engine_view.back()

    def forward(self):
        self.web_engine_view.forward()

    def reload(self):
        self.web_engine_view.reload()

    def home(self):
        self.web_engine_view.load(QUrl(self.initial_url))



def error_handler(etype, value, tb):
    error_msg = ''.join(traceback.format_exception(etype, value, tb))
    raise error_msg

sys.excepthook = error_handler

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())