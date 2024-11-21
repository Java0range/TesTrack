from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ConnectServer(object):
    def setupUi(self, ConnectServer):
        ConnectServer.setObjectName("ConnectServer")
        ConnectServer.resize(669, 445)
        ConnectServer.setStyleSheet("#centralwidget {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 175, 110, 255));\n"
"}\n"
"#frame {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 217, 0, 255), stop:1 rgba(255, 165, 92, 255));\n"
"border-radius: 20px;\n"
"}\n"
"QLineEdit {\n"
"    font: 8pt MS Shell Dlg 2;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 18px;\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=ConnectServer)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 60, 471, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(120, 140, 211, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(180, 180, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 31, 61))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./src/lock.png"))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 90, 211, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(80, 80, 31, 61))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./src/user.png"))
        self.label_3.setObjectName("label_3")
        ConnectServer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ConnectServer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdmin_Tools = QtWidgets.QMenu(parent=self.menubar)
        self.menuAdmin_Tools.setObjectName("menuAdmin_Tools")
        ConnectServer.setMenuBar(self.menubar)
        self.actionAdmin_Panel = QtGui.QAction(parent=ConnectServer)
        self.actionAdmin_Panel.setObjectName("actionAdmin_Panel")
        self.actionServer_Settings = QtGui.QAction(parent=ConnectServer)
        self.actionServer_Settings.setObjectName("actionServer_Settings")
        self.menuAdmin_Tools.addAction(self.actionAdmin_Panel)
        self.menuAdmin_Tools.addAction(self.actionServer_Settings)
        self.menubar.addAction(self.menuAdmin_Tools.menuAction())

        self.retranslateUi(ConnectServer)
        QtCore.QMetaObject.connectSlotsByName(ConnectServer)

    def retranslateUi(self, ConnectServer):
        _translate = QtCore.QCoreApplication.translate
        ConnectServer.setWindowTitle(_translate("ConnectServer", "TesTrack "))
        self.pushButton.setText(_translate("ConnectServer", "Вход"))
        self.menuAdmin_Tools.setTitle(_translate("ConnectServer", "Admin Tools"))
        self.actionAdmin_Panel.setText(_translate("ConnectServer", "Admin Panel"))
        self.actionServer_Settings.setText(_translate("ConnectServer", "Server Settings"))