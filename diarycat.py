import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtGui import QPixmap
import wearecats
from uis.uiformdiary import Ui_MainWindow


# Diary of a cat
class Diary(QMainWindow):
    def __init__(self, login):
        self.login = login
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.add_photo.clicked.connect(self.add_photo)
        self.ui.back.clicked.connect(self.back)

    def add_photo(self):  # Adding a photo of a cat
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                   "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.ui.label.setPixmap(pixmap.scaled(QSize(200, 200)))

    def back(self):  # Return to main menu
        self.we_are_cats = wearecats.WeAreCats(self.login)
        self.we_are_cats.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Diary()
    window.show()
    sys.exit(app.exec())
