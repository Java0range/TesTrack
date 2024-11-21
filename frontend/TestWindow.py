from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPainter, QPen, QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets


class PaintWidget(QLabel):
    def __init__(self, img, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.img = img
        self.pixmap = img
        self.active = False
        self.last_point = None
        self.is_painting = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

    def mouseMoveEvent(self, event):
        if self.is_painting and self.last_point is not None:
            painter = QPainter(self.pixmap)
            pen = QPen()
            pen.setWidth(3)
            pen.setColor(Qt.GlobalColor.black)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.position().toPoint())
            painter.end()
            self.update()
        self.last_point = event.position().toPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.active:
            self.is_painting = True
            self.last_point = event.position().toPoint()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_painting = False
            self.last_point = None

    def active_clicked(self):
        self.active = True if not self.active else False


class Ui_TestWindow(object):
    closed = pyqtSignal()
    def setupUi(self, TestWindow, imgurl):
        TestWindow.setObjectName("TestWindow")
        TestWindow.resize(1300, 831)
        self.widget = QtWidgets.QWidget(parent=TestWindow)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1301, 831))
        self.widget.setStyleSheet("#widget {\n"
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
"    background-color: rgb(255, 226, 0);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    padding: 6px;\n"
"    margin-top: 10px;\n"
"    border-radius: 15px;\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgb(221, 221, 221);\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"    background-color: rgb(221, 221, 221);\n"
"}")
        self.widget.setObjectName("widget")
        self.save_Button = QtWidgets.QPushButton(parent=self.widget)
        self.save_Button.setGeometry(QtCore.QRect(800, 770, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.save_Button.setFont(font)
        self.save_Button.setObjectName("save_Button")
        self.otvet_input = QtWidgets.QLineEdit(parent=self.widget)
        self.otvet_input.setGeometry(QtCore.QRect(500, 780, 291, 41))
        self.otvet_input.setObjectName("otvet_input")
        self.marker_Button = QtWidgets.QPushButton(parent=self.widget)
        self.marker_Button.setGeometry(QtCore.QRect(380, 770, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.marker_Button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/marker.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.marker_Button.setIcon(icon)
        self.marker_Button.setObjectName("marker_Button")
        self.label = PaintWidget(self.img_create(imgurl), parent=self.widget)
        self.label.setGeometry(QtCore.QRect(6, 3, 1291, 761))
        self.label.setText("")
        self.label.setObjectName("label")
        self.marker_Button.clicked.connect(self.marker_button_clicked)

        self.retranslateUi(TestWindow)
        QtCore.QMetaObject.connectSlotsByName(TestWindow)

    def retranslateUi(self, TestWindow):
        _translate = QtCore.QCoreApplication.translate
        TestWindow.setWindowTitle(_translate("TestWindow", "TesTrack"))
        self.save_Button.setText(_translate("TestWindow", "Сохранить ответ"))
        self.marker_Button.setText(_translate("TestWindow", "Маркер"))

    def marker_button_clicked(self):
        self.label.active_clicked()

    def img_create(self, imgurl):
        background = QPixmap(1291, 761)
        background.fill(Qt.GlobalColor.white)
        overlay = QPixmap(imgurl)
        bg_width = background.width()
        bg_height = background.height()
        ov_width = overlay.width()
        ov_height = overlay.height()
        result = QPixmap(bg_width, bg_height)
        painter = QPainter(result)
        painter.drawPixmap(0, 0, background)
        x_pos = (bg_width - ov_width) // 2
        y_pos = (bg_height - ov_height) // 2
        painter.drawPixmap(x_pos, y_pos, overlay)
        painter.end()
        return result

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()