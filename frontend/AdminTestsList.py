from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdminTestsList(object):
    def setupUi(self, AdminPanel):
        AdminPanel.setObjectName("AdminPanel")
        AdminPanel.resize(616, 507)
        self.widget = QtWidgets.QWidget(parent=AdminPanel)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.widget.setStyleSheet("#widget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 175, 110, 255));\n"
"}\n"
"#frame {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 217, 0, 255), stop:1 rgba(255, 165, 92, 255));\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 217, 0, 255), stop:1 rgba(255, 165, 92, 255));;\n"
"    padding: 6px;\n"
"    margin-top: 10px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"    background-color: rgb(221, 221, 221);\n"
"}")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(parent=self.widget)
        self.frame.setGeometry(QtCore.QRect(9, 430, 601, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 0, 51, 61))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/create.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(38, 38))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 0, 51, 61))
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./src/ok.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 0, 51, 61))
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./src/reload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(38, 38))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 0, 51, 61))
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./src/del.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 621, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslateUi(AdminPanel)
        QtCore.QMetaObject.connectSlotsByName(AdminPanel)

    def retranslateUi(self, AdminPanel):
        _translate = QtCore.QCoreApplication.translate
        AdminPanel.setWindowTitle(_translate("AdminPanel", "TesTrack"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdminPanel", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminPanel", "Name"))
