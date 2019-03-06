import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Example(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.load(QUrl('https://csumb.edu'))

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())