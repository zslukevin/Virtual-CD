# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(157, 48)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnEject = QtWidgets.QPushButton(self.centralwidget)
        self.btnEject.setObjectName("btnEject")
        self.horizontalLayout.addWidget(self.btnEject)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "虚拟光驱"))
        self.btnOpen.setToolTip(_translate("MainWindow", "加载ISO文件"))
        self.btnOpen.setText(_translate("MainWindow", "打开"))
        self.btnEject.setToolTip(_translate("MainWindow", "弹出ISO文件"))
        self.btnEject.setText(_translate("MainWindow", "弹出"))

