from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.B_100 = QtGui.QPushButton(self.centralwidget)
        self.B_100.setGeometry(QtCore.QRect(20, 10, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.B_100.setFont(font)
        self.B_100.setStyleSheet(_fromUtf8(""))
        self.B_100.setCheckable(True)
        self.B_100.setObjectName(_fromUtf8("B_100"))
        self.B_300 = QtGui.QPushButton(self.centralwidget)
        self.B_300.setGeometry(QtCore.QRect(540, 10, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.B_300.setFont(font)
        self.B_300.setStyleSheet(_fromUtf8(""))		
        self.B_300.setCheckable(True)		
        self.B_300.setObjectName(_fromUtf8("B_300"))
        self.B_200 = QtGui.QPushButton(self.centralwidget)
        self.B_200.setGeometry(QtCore.QRect(280, 10, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.B_200.setFont(font)
        self.B_200.setStyleSheet(_fromUtf8(""))		
        self.B_200.setObjectName(_fromUtf8("B_200"))
        self.B_200.setCheckable(True)		
        self.B_2 = QtGui.QPushButton(self.centralwidget)
        self.B_2.setCheckable(True)
        self.B_2.setGeometry(QtCore.QRect(280, 150, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_2.setFont(font)
        self.B_2.setObjectName(_fromUtf8("B_2"))
        self.B_3 = QtGui.QPushButton(self.centralwidget)
        self.B_3.setCheckable(True)
        self.B_3.setGeometry(QtCore.QRect(540, 150, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_3.setFont(font)
        self.B_3.setObjectName(_fromUtf8("B_3"))
        self.B_1 = QtGui.QPushButton(self.centralwidget)
        self.B_1.setCheckable(True)		
        self.B_1.setGeometry(QtCore.QRect(20, 150, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_1.setFont(font)
        self.B_1.setObjectName(_fromUtf8("B_1"))
        self.B_5 = QtGui.QPushButton(self.centralwidget)
        self.B_5.setCheckable(True)		
        self.B_5.setGeometry(QtCore.QRect(280, 230, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_5.setFont(font)
        self.B_5.setObjectName(_fromUtf8("B_5"))
        self.B_6 = QtGui.QPushButton(self.centralwidget)
        self.B_6.setCheckable(True)		
        self.B_6.setGeometry(QtCore.QRect(540, 230, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_6.setFont(font)
        self.B_6.setObjectName(_fromUtf8("B_6"))
        self.B_4 = QtGui.QPushButton(self.centralwidget)
        self.B_4.setCheckable(True)		
        self.B_4.setGeometry(QtCore.QRect(20, 230, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_4.setFont(font)
        self.B_4.setObjectName(_fromUtf8("B_4"))
        self.B_8 = QtGui.QPushButton(self.centralwidget)
        self.B_8.setCheckable(True)		
        self.B_8.setGeometry(QtCore.QRect(280, 310, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_8.setFont(font)
        self.B_8.setObjectName(_fromUtf8("B_8"))
        self.B_9 = QtGui.QPushButton(self.centralwidget)
        self.B_9.setCheckable(True)		
        self.B_9.setGeometry(QtCore.QRect(540, 310, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_9.setFont(font)
        self.B_9.setObjectName(_fromUtf8("B_9"))
        self.B_7 = QtGui.QPushButton(self.centralwidget)
        self.B_7.setCheckable(True)		
        self.B_7.setGeometry(QtCore.QRect(20, 310, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_7.setFont(font)
        self.B_7.setObjectName(_fromUtf8("B_7"))
        self.B_abbruch = QtGui.QPushButton(self.centralwidget)
        self.B_abbruch.setGeometry(QtCore.QRect(20, 390, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_abbruch.setFont(font)
        self.B_abbruch.setObjectName(_fromUtf8("B_abbruch"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 120, 751, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(590, 390, 121, 41))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 400, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospac821 BT"))
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
		
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.B_100.setText(_translate("MainWindow", "100 ml", None))
        self.B_300.setText(_translate("MainWindow", "300 ml", None))
        self.B_200.setText(_translate("MainWindow", "200 ml", None))
        self.B_2.setText(_translate("MainWindow", "Monkey Wrench", None))
        self.B_3.setText(_translate("MainWindow", "Painkiller", None))
        self.B_1.setText(_translate("MainWindow", "Captain Cola", None))
        self.B_5.setText(_translate("MainWindow", "SwimmingPool", None))
        self.B_6.setText(_translate("MainWindow", "Wodka Sunrise", None))
        self.B_4.setText(_translate("MainWindow", "Wodka-O", None))
        self.B_8.setText(_translate("MainWindow", "Chi-Chi", None))
        self.B_9.setText(_translate("MainWindow", "Zombie", None))
        self.B_7.setText(_translate("MainWindow", "Long Island Icetea", None))
        self.B_abbruch.setText(_translate("MainWindow", "Abbruch", None))
        self.label.setText(_translate("MainWindow", "Liter", None))