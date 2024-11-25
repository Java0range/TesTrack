from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdminTestList(object):
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
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 621, 511))
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
        item.setText(_translate("AdminPanel", "User id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminPanel", "Result"))
