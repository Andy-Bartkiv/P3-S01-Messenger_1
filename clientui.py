# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 60, 401, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.MessageWindow = QtWidgets.QTextEdit(self.centralwidget)
        self.MessageWindow.setGeometry(QtCore.QRect(10, 310, 321, 31))
        self.MessageWindow.setAutoFillBackground(False)
        self.MessageWindow.setObjectName("MessageWindow")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 310, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 30, 181, 19))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "A-Chat Messenger"))
        self.MessageWindow.setPlaceholderText(_translate("MainWindow", "Enter your message here"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Login"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
