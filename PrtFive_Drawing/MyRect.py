from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt


class MyRect(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent):
        print(event.key())
        if event.key() == Qt.Key.Key_Left:
            self.setPos(self.x() - 10, self.y())
        elif event.key() == Qt.Key.Key_Right:
            self.setPos(self.x() + 10, self.y())
        elif event.key() == Qt.Key.Key_Up:
            self.setPos(self.x(), self.y() - 10)
        elif event.key() == Qt.Key.Key_Down:
            self.setPos(self.x(), self.y() + 10)


