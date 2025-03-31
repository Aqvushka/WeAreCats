import sys
import random

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QStyle
import wearecats
from uis.test import Ui_MainWindow


# Window with the test "What kind of cat are you
class Test(QMainWindow):
    def __init__(self, login):
        self.login = login
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.final_test.clicked.connect(self.final_test)
        self.ui.back.clicked.connect(self.back)
        self.button_groups = [self.ui.buttonGroup, self.ui.buttonGroup_2, self.ui.buttonGroup_3, self.ui.buttonGroup_4,
                              self.ui.buttonGroup_5, self.ui.buttonGroup_6, self.ui.buttonGroup_7,
                              self.ui.buttonGroup_8]

    def final_test(
            self):  # When you click on the "final_test" button, a random result is generated from the list of answers
        answers = ['Вы очень хороший котик!', 'Вы - котик - милашка!', 'Вы котик!',
                   'Вы точно котик?', 'Мяу-мяу! Мяу? Мяу-мяу-мяу!',
                   'Тсс, это тайна', '*цомк*', 'Рыбка уже в миске)', 'Вы котик - шалун', 'Вы - котик - ласкуша',
                   'Вы котик - соня!', 'Вы котик - вредняка!', 'Вы пушистый милашка!',
                   'Вы рыб о.о', 'О нет... Вы - человек...', 'Вы сонный котик :)']
        score = 0

        for button_group in self.button_groups:
            id = 0
            for button in button_group.buttons():
                id += 1
                button_group.setId(button, id)

        for button_group in self.button_groups:
            for button in button_group.buttons():
                if button.isChecked():
                    score += button_group.id(button)
        self.ui.statusbar.setStyleSheet('color: green')
        self.ui.statusbar.showMessage(f'{answers[score // 2 - 1]}')
        self.ui.label_9.setPixmap(QPixmap(f'answers/a{score // 2 + 1}.jpg').scaled(QSize(291, 341)))

    def back(self):  # Go to main menu
        self.we_are_cats = wearecats.WeAreCats(self.login)
        self.we_are_cats.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec())
