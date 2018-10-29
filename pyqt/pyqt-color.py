import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(227, 66, 52))
        self.setPalette(p)

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())