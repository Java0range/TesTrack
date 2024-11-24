from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_create_test_2(object):
    def setupUi(self, create_test_2):
        create_test_2.setObjectName("create_test_2")
        create_test_2.resize(390, 410)
        create_test_2.setStyleSheet("QDialog {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 175, 110, 255));\n"
"}\n"
"#widget {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 217, 0, 255), stop:1 rgba(255, 165, 92, 255));\n"
"    border-radius: 20px;\n"
"}\n"
"QLineEdit {\n"
"    font: 8pt MS Shell Dlg 2;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 217, 0, 255), stop:1 rgba(255, 165, 92, 255));;\n"
"    padding: 6px;\n"
"    margin-top: 10px;\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgb(221, 221, 221);\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"    background-color: rgb(221, 221, 221);\n"
"}")
        self.tableWidget = QtWidgets.QTableWidget(parent=create_test_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 391, 361))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton = QtWidgets.QPushButton(parent=create_test_2)
        self.pushButton.setGeometry(QtCore.QRect(120, 360, 141, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(create_test_2)
        QtCore.QMetaObject.connectSlotsByName(create_test_2)

    def retranslateUi(self, create_test_2):
        _translate = QtCore.QCoreApplication.translate
        create_test_2.setWindowTitle(_translate("create_test_2", "TesTrack"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("create_test_2", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("create_test_2", "Ссылка на картинку"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("create_test_2", "Правильный ответ"))
        self.pushButton.setText(_translate("create_test_2", "Сохранить"))
