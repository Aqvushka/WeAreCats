import sys
from idlelib.iomenu import encoding

import pandas as pd
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from check_password import *
from uis.reg import Ui_MainWindow
import wearecats


# Registration/Authentication Window
class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.users = self.load_users_from_csv('logins.csv')

    def initUI(self):
        self.ui.login.clicked.connect(self.login)
        self.ui.registration.clicked.connect(self.register)


    def load_users_from_csv(self, file):
        df = pd.read_csv(file)
        return df

    def login(self):
        login = self.ui.loginEdit.text()
        password = self.ui.passwordEdit.text()
        some = self.users.loc[self.users['login'] == login, ' password']
        try:
            if (self.users.loc[self.users['login'] == login, ' password'])[some.index[0]][
               1:] == password:  # Checking the match between the entered password and the password from the database
                self.open_we_are_cats(login)  # If successful, the main application menu opens
            else:
                self.ui.statusbar.setStyleSheet('color: orange')  # If it fails, an error is written
                self.ui.statusbar.showMessage('Ошибка: Неправильный логин или пароль!')
        except Exception as e:
            self.ui.statusbar.setStyleSheet('color: orange')  # If it fails, an error is written
            self.ui.statusbar.showMessage('Ошибка: Неправильный логин или пароль!')

    def register(self):  # Adding a new user to the logins database
        login = self.ui.loginEdit.text()
        password = self.ui.passwordEdit.text()
        try:
            check_password(password)  # Checking Password Compliance
            if login in self.users:  # Checking for login availability in the database
                self.ui.statusbar.setStyleSheet(
                    'color: red')  # Refusal to register a user whose login is already in the database
                self.ui.statusbar.showMessage('Логин уже существует')
            else:
                new_user_df = pd.DataFrame({'login': [login], ' password': [' ' + password]})
                user_df = pd.read_csv('logins.csv')
                user_df = pd.concat([user_df, new_user_df], ignore_index=True)
                user_df.to_csv('logins.csv', index=False)
                self.users = self.load_users_from_csv('logins.csv')
                self.ui.statusbar.setStyleSheet('color: green')
                self.ui.statusbar.showMessage('Регистрация успешна!')
        except Exception as e:
            self.ui.statusbar.setStyleSheet('color: red')
            self.ui.statusbar.showMessage(f'Ошибка при регистрации: {e}')

    def open_we_are_cats(self, name):
        self.we_are_cats = wearecats.WeAreCats(name)  # Opening the main application window
        self.we_are_cats.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec())
