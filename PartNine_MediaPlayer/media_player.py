import traceback
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout,\
    QStyle, QSlider, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
import sys
import os


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.basedir = os.path.dirname(__file__)
        self.setWindowTitle('PyQT6 Media Player')
        self.setWindowIcon(QIcon(os.path.join(self.basedir, "images", 'player.ico')))

        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)

        self.video_widget = QVideoWidget()
        # Open button
        self.button_open = QPushButton('Open Video')
        self.button_open.clicked.connect(self.open_video)

        # Play button
        self.button_play = QPushButton()
        self.button_play.setEnabled(False)
        self.button_play.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.button_play.clicked.connect(self.play_video)

        # Slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # Media player signals
        self.media_player.mediaStatusChanged.connect(self.media_state_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button_open)
        hbox.addWidget(self.button_play)
        hbox.addWidget(self.slider)
        vbox = QVBoxLayout()
        vbox.addWidget(self.video_widget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.media_player.setVideoOutput(self.video_widget)

    def open_video(self):
        file_name, _ = QFileDialog.getOpenFileNames(self, 'Open File')
        print(file_name)

        if file_name[0] != '':
            self.media_player.setSource(QUrl.fromLocalFile(file_name[0]))
            self.button_play.setEnabled(True)

    def play_video(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()

        else:
            self.media_player.play()

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def media_state_changed(self):
        if self.media_player.PlaybackState == QMediaPlayer.PlaybackState.PlayingState:
            self.button_play.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        else:
            self.button_play.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))


def error_handler(etype, value, tb):
    error_msg = ''.join(traceback.format_exception(etype, value, tb))
    raise error_msg

sys.excepthook = error_handler

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
