from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Rez_Window(object):
    def setupUi(self, Rez_Window):
        Rez_Window.setObjectName("Rez_Window")
        Rez_Window.resize(629, 572)
        self.tableWidget = QtWidgets.QTableWidget(parent=Rez_Window)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 631, 571))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Rez_Window)
        QtCore.QMetaObject.connectSlotsByName(Rez_Window)

    def retranslateUi(self, Rez_Window):
        _translate = QtCore.QCoreApplication.translate
        Rez_Window.setWindowTitle(_translate("Rez_Window", "TesTrack"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Rez_Window", "Задание"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Rez_Window", "Ваш ответ"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Rez_Window", "Правильный ответ"))
