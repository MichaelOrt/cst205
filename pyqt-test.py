import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DEFAULT')
        self.show()

mainWin = MainWindow()
input("Press enter")
mainWin.setWindowTitle("CST 205 Main Window")
status = app.exec_()
sys.exit(status)