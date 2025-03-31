import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
import wearecats
from uis.uiformencyclopedia import Ui_MainWindow


# Window with an encyclopedia about different breeds of cats
class Encyclopedia(QMainWindow):
    def __init__(self, login):
        self.login = login
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.back.clicked.connect(self.back)

    def back(self):  # Return to main menu
        self.we_are_cats = wearecats.WeAreCats(self.login)
        self.we_are_cats.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Encyclopedia()
    window.show()
    sys.exit(app.exec())
