import os
import sys
from idlelib.iomenu import encoding
from sys import prefix

import pandas as pd
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QLabel, QMessageBox
import wearecats
from uis import conn, uiformcatDB


# Window for viewing the cat database
class Connect(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.ui = conn.Ui_MainWindow()
        self.ui.setupUi(self)
        self.name = name
        self.initUI()

    def initUI(self):
        self.ui.back.clicked.connect(self.back)
        self.load_info()

    def back(self):
        self.close()

    def load_info(self):
        try:
            df = pd.read_csv('shelters.csv', encoding='cp1251')
            data = df.iloc[df.loc[df['name'] == self.name].index]
            data = data.values.tolist()
            address = data[0][2]
            number = data[0][3]
            self.ui.nameEdit.setText(self.name)
            self.ui.addressEdit.setText(address)
            self.ui.numberEdit.setText(number)
        except Exception as e:
            QMessageBox.information(self, 'Нету', 'Такого приюта нет')
            self.close()


class FindCat(QMainWindow):
    def __init__(self, login):
        super().__init__()
        self.ui = uiformcatDB.Ui_MainWindow()
        self.login = login
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.info_about_shelter.clicked.connect(self.connection)
        self.ui.back.clicked.connect(self.back)
        self.ui.cat_taken.clicked.connect(self.cat_taken)
        self.ui.filter_shelter.clicked.connect(self.filter_by_shelter)
        self.is_shelter_owner()
        self.load_csv('cats.csv')

    def cat_taken(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            try:
                shelter = pd.read_csv('shelters.csv', encoding='cp1251')
                # Select a row where shelter belongs to login
                shelter = shelter.iloc[shelter.loc[shelter['login'] == self.login].index]
                shelter = shelter.values.tolist()[0][1]  # Returns shelter name
                cats = pd.read_csv('cats.csv', encoding='cp1251')
                name = self.ui.tableWidget.item(selected_row, 0).text()  # Cat's name
                cats = cats.iloc[cats.loc[cats['shelter'] == shelter].index]  # All cats from user's shelter
                selected_cat = ''
                for cat in cats.values.tolist():  # Iterate thru to find earlier selected cat
                    if cat[0] == name:
                        selected_cat = cat[0]
                # Specific cat from this shelter with this name
                sd = (cats[cats['name'] == selected_cat])[cats['shelter'] == shelter].index
                index = sd.values.tolist()[0]  # Index of selected cat in general database
                cats = cats.drop(index)  # Delete cat :(
                cats.to_csv('cats.csv', encoding='cp1251', index=False)  # Save without cat :(
                self.load_csv('cats.csv')  # Update table to once again show all available cats
            except IndexError as e:
                self.ui.statusbar.setStyleSheet('color: red')
                self.ui.statusbar.showMessage(f'Ошибка: выберите кота из своего приюта')
        else:
            self.ui.statusbar.setStyleSheet('color: red')
            self.ui.statusbar.showMessage(f'Ошибка: выберите кота')

    def filter_by_shelter(self):
        cats = pd.read_csv('cats.csv', encoding='cp1251')
        shelters = pd.read_csv('shelters.csv', encoding='cp1251')
        shelter = shelters.iloc[shelters.loc[shelters['login'] == self.login].index]
        shelter = shelter.values.tolist()[0][1]  # Finds a shelter associated with user
        data = cats.iloc[cats.loc[cats['shelter'] == shelter].index]  # Makes a list of cats in shelter
        data = data.values.tolist()
        self.ui.tableWidget.clearContents()  # Clears table from all cats :(
        self.ui.tableWidget.setRowCount(len(data))
        # Fill a table with cats from shelter
        for row_index, row in enumerate(data):
            self.ui.tableWidget.setRowHeight(row_index, 100)
            for col_index, cell in enumerate(row):
                if col_index == 4:
                    if os.path.isfile(str(cell)):
                        image = str(cell)
                    else:
                        image = 'defaultcat.jpg'
                    label = QLabel()
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap.scaled(QSize(100, 100)))
                    self.ui.tableWidget.setCellWidget(row_index, col_index, label)
                else:
                    self.ui.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(cell)))

    def is_shelter_owner(self):  # Hides cat taken and filer buttons from users not associated with shelter
        try:
            df = pd.read_csv('shelters.csv', encoding='cp1251')
            data = df.iloc[df.loc[df['login'] == self.login].index]
            data = data.values.tolist()
            if not data:
                self.ui.filter_shelter.hide()
                self.ui.cat_taken.hide()
        except Exception as e:
            pass

    def load_csv(self, csv_file):
        df = pd.read_csv(csv_file, encoding='cp1251')
        self.ui.tableWidget.setRowCount(len(df))
        for row_index, row in df.iterrows():
            self.ui.tableWidget.setRowHeight(row_index, 100)
            for col_index, cell in enumerate(row):
                if col_index == 4:
                    if os.path.isfile(str(cell)):
                        image = str(cell)
                    else:
                        image = 'defaultcat.jpg'
                    label = QLabel()
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap.scaled(QSize(100, 100)))
                    self.ui.tableWidget.setCellWidget(row_index, col_index, label)
                else:
                    self.ui.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(cell)))

    def connection(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            name = self.ui.tableWidget.item(selected_row, 1).text()
            self.conn_window = Connect(name)  # View shelter information for the selected cat
            self.conn_window.show()

    def back(self):
        self.we_are_cats = wearecats.WeAreCats(self.login)  # Return to the main application menu
        self.we_are_cats.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FindCat('qwerty')
    window.show()
    sys.exit(app.exec())
