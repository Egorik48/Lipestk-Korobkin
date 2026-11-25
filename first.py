import io
import random
import sys

from PyQt6 import uic
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtWidgets import QWidget, QApplication


class Square1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.do_paint = True

        self.color = QColor(255, 255, 0)

        self.pushButton.clicked.connect(self.trigger_paint)

    def trigger_paint(self):
        self.do_paint = True
        self.update()  # Просим Qt перерисовать виджет

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ell(qp)
            qp.end()
            self.do_paint = False

    def draw_ell(self, qp):
        pen = QPen()
        pen.setColor(self.color)
        qp.setPen(pen)
        square = QRectF(50, 40, a := random.randint(100, 200), a)
        square1 = QRectF(150, 140, a := random.randint(100, 200), a)
        qp.drawEllipse(square)
        qp.drawEllipse(square1)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Square1()
    ex.show()
    sys.exit(app.exec())