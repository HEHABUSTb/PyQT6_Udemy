from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, \
    QGraphicsRectItem, QGraphicsItem
import sys
from MyRect import MyRect


class Window(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800,600)
        self.show()

        scene = QGraphicsScene()

        #create rect item
        #rect = QGraphicsRectItem()

        rect = MyRect()
        rect.setRect(0,0, 100,100)
        scene.addItem(rect)

        #make rect focusable
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        rect.setFocus()

        self.setScene(scene)


app = QApplication([])
window = Window()
sys.exit(app.exec())
