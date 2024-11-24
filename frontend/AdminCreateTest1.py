from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_create_test_1(object):
    def setupUi(self, create_test_1):
        create_test_1.setObjectName("create_test_1")
        create_test_1.resize(304, 283)
        create_test_1.setStyleSheet("#centralwidget {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=create_test_1)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 19, 261, 251))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(60, 140, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 50, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 110, 181, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(create_test_1)
        QtCore.QMetaObject.connectSlotsByName(create_test_1)

    def retranslateUi(self, create_test_1):
        _translate = QtCore.QCoreApplication.translate
        create_test_1.setWindowTitle(_translate("create_test_1", "TesTrack"))
        self.pushButton.setText(_translate("create_test_1", "Далее"))
        self.label_2.setText(_translate("create_test_1", "Введите название теста"))
        self.label_3.setText(_translate("create_test_1", "Введите кол-во вопросов"))
