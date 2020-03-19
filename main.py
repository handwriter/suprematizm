from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
import sys
from PIL.ImageQt import ImageQt
from PIL import Image, ImageDraw
from random import randint
from design import Ui_Form as Design
from PyQt5 import QtGui
from PyQt5.QtGui import QCursor

class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pos = None
        self.pixmap = QPixmap()
        self.image = Image.new('RGBA', (800, 800))
        self.draw = ImageDraw.Draw(self.image)

    def triangle(self, pos):
        try:
            self.draw.polygon([(QCursor.pos().x() - 20 - 560, QCursor.pos().y() - 20 - 167), (QCursor.pos().x() - 560, QCursor.pos().y() - 167),
                          (QCursor.pos().x() + 20 - 560, QCursor.pos().y() - 20 - 167)], fill = "green")
        except:
            pass
        self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))

    def circle(self, ev):
        try:
            self.draw.ellipse((ev.pos().x() - 30 - 31, ev.pos().y() - 30 - 10, ev.pos().x() + 30 - 31, ev.pos().y() + 30 - 10), fill = "red")
        except:
            pass
        self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))

    def rectangle(self, ev):
        try:
            self.draw.rectangle((ev.pos().x() - 30 - 31, ev.pos().y() - 30, ev.pos().x() + 30 - 31, ev.pos().y() + 30), fill = "black")
        except:
            pass
        self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == 32:
            self.triangle(a0)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.button() == 1:
            self.circle(a0)
        elif a0.button() == 2:
            self.rectangle(a0)


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())