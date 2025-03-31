import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
import wearecats
from uis.uiformexit import Ui_MainWindow


# Application close window
class Exit(QMainWindow):
    def __init__(self, login):
        self.login = login
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.y_exit.clicked.connect(self.exit)
        self.ui.n_exit.clicked.connect(self.back)

    def exit(self):  # If "Yes" is selected, the application closes
        QApplication.quit()

    def back(self):  # If "No" is selected, the program returns to the main menu
        self.we_are_cats = wearecats.WeAreCats(self.login)
        self.we_are_cats.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Exit()
    window.show()
    sys.exit(app.exec())
