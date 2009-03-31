# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pooky.ui'
#
# Created: Tue Mar 31 07:18:21 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 572)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../pictures/icons/black and white/16x16/actions/wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(359, 1, 371, 539))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.code = QtGui.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        self.code.setFont(font)
        self.code.setObjectName("code")
        self.verticalLayout_2.addWidget(self.code)
        self.registers = QtGui.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        self.registers.setFont(font)
        self.registers.setObjectName("registers")
        self.verticalLayout_2.addWidget(self.registers)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.filename = QtGui.QLabel(self.layoutWidget)
        self.filename.setObjectName("filename")
        self.verticalLayout.addWidget(self.filename)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start = QtGui.QPushButton(self.layoutWidget)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.stop = QtGui.QPushButton(self.layoutWidget)
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        self.step = QtGui.QPushButton(self.layoutWidget)
        self.step.setObjectName("step")
        self.horizontalLayout.addWidget(self.step)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 351, 541))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stdout = QtGui.QTextBrowser(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(12)
        self.stdout.setFont(font)
        self.stdout.setObjectName("stdout")
        self.verticalLayout_3.addWidget(self.stdout)
        self.stdin = QtGui.QLabel(self.layoutWidget1)
        self.stdin.setObjectName("stdin")
        self.verticalLayout_3.addWidget(self.stdin)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNull = QtGui.QAction(MainWindow)
        self.actionNull.setObjectName("actionNull")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pooky Ook! interpreter", None, QtGui.QApplication.UnicodeUTF8))
        self.start.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.step.setText(QtGui.QApplication.translate("MainWindow", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.stdin.setText(QtGui.QApplication.translate("MainWindow", "stdin: ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNull.setText(QtGui.QApplication.translate("MainWindow", "Null", None, QtGui.QApplication.UnicodeUTF8))

