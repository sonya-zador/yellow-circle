import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circle.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def draw_flag(self, qp):
        r = int(random.randint(0, 500))
        g = int(random.randint(0, 500))
        qp.drawEllipse(r, g, 90, 90)
        qp.setBrush(QColor(250, 250, 0))

    def paint(self):
        self.do_paint = True
        self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())