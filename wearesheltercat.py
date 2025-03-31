import sys
import shutil
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
import wearecats
import pandas as pd
from uis import add, weareshelter


# Window for shelters - information about them and adding cats to the general database of cats
class Add(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = add.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):

        #If the user login is in the shelter logins, information about the shelter will be displayed (change is not available)
        self.ui.add.clicked.connect(self.add)
        self.ui.back.clicked.connect(self.back)
        self.ui.add_photo.clicked.connect(self.add_photo)
        self.file_path = ''

    def add(self):  # Adding a cat to the database
        new_row = pd.DataFrame({
            'name': [self.ui.nameEdit.text()],
            'shelter': [self.ui.shelterEdit.text()],
            'breed': [self.ui.breedEdit.text()],
            'age': [self.ui.ageEdit.text()],
            'photo': [self.file_path]
        })
        existing_data = pd.read_csv('cats.csv', encoding='cp1251')
        updated_data = pd.concat([existing_data, new_row], ignore_index=True)
        updated_data.to_csv('cats.csv',encoding='cp1251', index=False)

    def back(self):  # Closing the add window
        self.close()

    def add_photo(self):  # Saving the path to the cat image
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                        "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)")
        try:
            shutil.copy(self.file_path, f'catsphoto/{self.file_path.split('/')[-1]}')
            self.file_path = f'catsphoto/{self.file_path.split('/')[-1]}'
        except Exception as e:
            pass


class Shelter(QMainWindow):
    def __init__(self, login):
        super().__init__()
        self.ui = weareshelter.Ui_MainWindow()
        self.ui.setupUi(self)
        self.login = login
        self.initUI()

    def initUI(self):

        self.ui.add_cat.clicked.connect(self.add_cat)
        self.ui.back.clicked.connect(self.back)
        try:
            df = pd.read_csv('shelters.csv', encoding='cp1251')
            data = df.iloc[df.loc[df['login'] == self.login].index]
            data = data.values.tolist()
            name = data[0][1]
            address = data[0][2]
            number = data[0][3]
            self.ui.nameEdit.setText(name)
            self.ui.addressEdit.setText(address)
            self.ui.numberEdit.setText(number)
        except Exception as e:
            pass


    def add_cat(self):  # Go to the window for adding a new cat to the cat database
        self.add = Add()
        self.add.show()

    def back(self):  # Return to main menu
        self.we_are_cats = wearecats.WeAreCats(self.login)
        self.we_are_cats.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Shelter()
    window.show()
    sys.exit(app.exec())
