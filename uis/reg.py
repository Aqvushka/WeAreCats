# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(668, 507)
        MainWindow.setStyleSheet("background-color: rgb(255, 238, 226);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 271, 431))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("reg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 160, 31, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 120, 131, 31))
        self.label_3.setObjectName("label_3")
        self.passwordEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(380, 220, 221, 21))
        self.passwordEdit.setText("")
        self.passwordEdit.setObjectName("passwordEdit")
        self.loginEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.loginEdit.setGeometry(QtCore.QRect(380, 190, 221, 21))
        self.loginEdit.setText("")
        self.loginEdit.setObjectName("loginEdit")
        self.login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login.setGeometry(QtCore.QRect(410, 250, 151, 21))
        self.login.setObjectName("login")
        self.registration = QtWidgets.QPushButton(parent=self.centralwidget)
        self.registration.setGeometry(QtCore.QRect(410, 280, 151, 21))
        self.registration.setObjectName("registration")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Вход</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Мы котики</span></p></body></html>"))
        self.passwordEdit.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.loginEdit.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.login.setText(_translate("MainWindow", "Я уже котик"))
        self.registration.setText(_translate("MainWindow", "Хочу в котики"))
