# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1232, 811)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(62, 62, 62);\n"
"color:rgb(232, 232, 232)")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listView_series = QtWidgets.QListView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listView_series.setFont(font)
        self.listView_series.setStyleSheet("background-color:rgb(50, 50, 50)")
        self.listView_series.setObjectName("listView_series")
        self.gridLayout.addWidget(self.listView_series, 1, 1, 1, 7)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setMinimumSize(QtCore.QSize(71, 31))
        self.pushButton_search.setMaximumSize(QtCore.QSize(71, 31))
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 0, 1, 1, 1)
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setMinimumSize(QtCore.QSize(261, 31))
        self.lineEdit_search.setMaximumSize(QtCore.QSize(261, 16777215))
        self.lineEdit_search.setText("")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout.addWidget(self.lineEdit_search, 0, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setMaximumSize(QtCore.QSize(261, 16777215))
        self.listView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listView.setStyleSheet("background-color:rgb(50, 50, 50)")
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.pushButton_download = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_download.setMinimumSize(QtCore.QSize(71, 31))
        self.pushButton_download.setMaximumSize(QtCore.QSize(71, 31))
        self.pushButton_download.setObjectName("pushButton_download")
        self.gridLayout.addWidget(self.pushButton_download, 0, 7, 1, 1)
        self.pushButton_copyUrl = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copyUrl.setMinimumSize(QtCore.QSize(71, 31))
        self.pushButton_copyUrl.setMaximumSize(QtCore.QSize(71, 31))
        self.pushButton_copyUrl.setObjectName("pushButton_copyUrl")
        self.gridLayout.addWidget(self.pushButton_copyUrl, 0, 6, 1, 1)
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setMinimumSize(QtCore.QSize(71, 31))
        self.pushButton_play.setMaximumSize(QtCore.QSize(71, 31))
        self.pushButton_play.setObjectName("pushButton_play")
        self.gridLayout.addWidget(self.pushButton_play, 0, 5, 1, 1)
        self.comboBox_way = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_way.setMinimumSize(QtCore.QSize(71, 31))
        self.comboBox_way.setMaximumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.comboBox_way.setFont(font)
        self.comboBox_way.setObjectName("comboBox_way")
        self.comboBox_way.addItem("")
        self.comboBox_way.addItem("")
        self.gridLayout.addWidget(self.comboBox_way, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1232, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "soand"))
        self.pushButton_search.setText(_translate("MainWindow", "search"))
        self.pushButton_download.setText(_translate("MainWindow", "Download"))
        self.pushButton_copyUrl.setText(_translate("MainWindow", "copyUrl"))
        self.pushButton_play.setText(_translate("MainWindow", "play"))
        self.comboBox_way.setItemText(0, _translate("MainWindow", "potPlayer"))
        self.comboBox_way.setItemText(1, _translate("MainWindow", "webDownload"))
