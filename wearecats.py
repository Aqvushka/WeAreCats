import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

# The main window of the application, from which you can navigate to all other tabs
from uis.main import Ui_MainWindow

import catDBcat
import wearesheltercat
import testcat
import encyclopediacat
import diarycat
import exitcat


class WeAreCats(QMainWindow):
    def __init__(self, login):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.login = login
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.find_cat.clicked.connect(self.open_find_cat)
        self.ui.shelter.clicked.connect(self.open_shelter)
        self.ui.test.clicked.connect(self.open_test)
        self.ui.encyclopedia.clicked.connect(self.open_encyclopedia)
        self.ui.diary.clicked.connect(self.open_diary)
        self.ui.exit.clicked.connect(self.to_exit)

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape:
            self.to_exit()

    def open_find_cat(self):  # Opening a window with a cat database
        self.find_cat = catDBcat.FindCat(self.login)
        self.find_cat.show()
        self.close()

    def open_shelter(
            self):  # Opening a window with information about the shelter (if the login is in the shelter database)
        self.shelter = wearesheltercat.Shelter(self.login)
        self.shelter.show()
        self.close()

    def open_test(self):  # Opening the test "What kind of cat are you"
        self.test = testcat.Test(self.login)
        self.test.show()
        self.close()

    def open_encyclopedia(self):  # Opening an encyclopedia about different cat breeds (being finalized)
        self.encyclopedia = encyclopediacat.Encyclopedia(self.login)
        self.encyclopedia.show()
        self.close()

    def open_diary(self):  # Opening a cat's diary
        self.diary = diarycat.Diary(self.login)
        self.diary.show()
        self.close()

    def to_exit(self):  # Closing the application
        self.to_exit = exitcat.Exit(self.login)
        self.to_exit.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeAreCats()
    window.show()
    sys.exit(app.exec())
