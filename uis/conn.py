# Form implementation generated from reading ui file 'conn.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 339)
        MainWindow.setStyleSheet("background-color: rgb(255, 238, 226);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(120, 110, 181, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.addressEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.addressEdit.setGeometry(QtCore.QRect(120, 140, 181, 20))
        self.addressEdit.setObjectName("addressEdit")
        self.numberEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.numberEdit.setGeometry(QtCore.QRect(120, 170, 181, 20))
        self.numberEdit.setObjectName("numberEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 261, 61))
        self.label.setObjectName("label")
        self.back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back.setGeometry(QtCore.QRect(170, 210, 75, 23))
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Свзяаться с приютом</span></p></body></html>"))
        self.back.setText(_translate("MainWindow", "Вернуться"))
