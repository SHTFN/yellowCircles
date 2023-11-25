import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        for i in range(randint(1, 5)):
            r = randint(1, 450)
            qp.setBrush(QColor(255, 255, 153))
            qp.drawEllipse(randint(1, 250), randint(1, 250), r, r)

    def paint(self):
        self.do_paint = True
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
