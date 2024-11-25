from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreateUser(object):
    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("AuthWindow")
        AuthWindow.resize(342, 234)
        AuthWindow.setStyleSheet("#centralwidget {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 175, 110, 255));\n"
"}\n"
"#frame {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 217, 0, 255), stop:1 rgba(255, 165, 92, 255));\n"
"border-radius: 20px;\n"
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
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"    background-color: rgb(221, 221, 221);\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgb(221, 221, 221);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=AuthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 281, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.login_button = QtWidgets.QPushButton(parent=self.frame)
        self.login_button.setGeometry(QtCore.QRect(70, 100, 141, 41))
        self.login_button.setObjectName("login_button")
        self.server_inp = QtWidgets.QLineEdit(parent=self.frame)
        self.server_inp.setGeometry(QtCore.QRect(50, 30, 181, 31))
        self.server_inp.setObjectName("server_inp")
        self.key_inp = QtWidgets.QLineEdit(parent=self.frame)
        self.key_inp.setGeometry(QtCore.QRect(50, 70, 181, 31))
        self.key_inp.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.key_inp.setObjectName("key_inp")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 51))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./src/user.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 31, 51))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./src/lock.png"))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBox.setGeometry(QtCore.QRect(110, 150, 71, 21))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "TesTrack"))
        self.login_button.setText(_translate("AuthWindow", "Create"))
        self.checkBox.setText(_translate("AuthWindow", "Admin"))
