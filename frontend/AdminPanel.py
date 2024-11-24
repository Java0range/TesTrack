from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdminPanel(object):
    def setupUi(self, AdminPanel):
        AdminPanel.setObjectName("AdminPanel")
        AdminPanel.resize(446, 169)
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
        self.frame.setGeometry(QtCore.QRect(19, 19, 411, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 10, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./src/test.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(AdminPanel)
        QtCore.QMetaObject.connectSlotsByName(AdminPanel)

    def retranslateUi(self, AdminPanel):
        _translate = QtCore.QCoreApplication.translate
        AdminPanel.setWindowTitle(_translate("AdminPanel", "TesTrack"))
        self.pushButton.setText(_translate("AdminPanel", "Пользователи"))
        self.pushButton_2.setText(_translate("AdminPanel", "Тесты"))
