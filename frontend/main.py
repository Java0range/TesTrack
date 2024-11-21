from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal
from ConnectWindow import Ui_ConnectServer
from TestList import Ui_TestList
from TestWindow import Ui_TestWindow
from PyQt6.QtWidgets import QMessageBox
import sys
import requests


class User:
    def __init__(self):
        self.link = "http://127.0.0.1:8000"
        self.admin = False
        self.test_id = 1
        self.test_window = 0

    def edit_admin(self, lvl):
        self.admin = lvl

    def edit_test_id(self, id):
        self.test_id = id

    def test_window_plus(self):
        self.test_window += 1



class MainWindow(QMainWindow, Ui_ConnectServer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.auth)

    def auth(self):
        name = self.lineEdit_3.text()
        password = self.lineEdit.text()
        link = f"{user.link}/users/auth/"

        data = {
            "username": name,
            "password": password
        }
        responce = requests.post(link, json=data)
        user.edit_admin(True if responce.json()["admin"] else False)
        match responce.json()["msg"]:
            case "true":
                self.testlist = TestList(self)
                self.testlist.show()
                ex.close()
            case "false":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Critical)
                msg_box.setText("Ошибка")
                msg_box.setWindowTitle("Ошибка")
                msg_box.exec()


class TestList(QDialog, Ui_TestList):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 500)
        self.pushButton_2.clicked.connect(self.test_clicked)
        try:
            link = f"{user.link}/tests/tests/"
            responce = requests.get(link).json()["msg"]
            for i in responce:
                numRows = self.tableWidget.rowCount()
                self.tableWidget.insertRow(numRows)
                self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(i[1])))
                self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(i[0]))
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.exec()

    def test_clicked(self):
        row = self.tableWidget.currentRow()
        test_id = int(self.tableWidget.item(row, 0).text())
        user.edit_test_id(test_id)
        try:
            link = f"{user.link}/tests/test/"
            data = {
                "test_id": test_id
            }
            responce = requests.post(link, json=data).json()["msg"]
            for i in responce:
                self.save_img(i[0])
            self.window_list = []
            for title in responce:
                window = TestWindow(f"./src/temp/{title[0]}")
                window.closed.connect(self.on_window_closed)
                self.window_list.append(window)

            if len(self.window_list) > 0:
                self.current_index = 0
                self.open_next_window()
            self.main.testlist.close()

        except Exception as error:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.exec()
            print(error)

    def save_img(self, imgurl):
        filename = f"./src/temp/{imgurl}"
        link = f"{user.link}/files/download/{imgurl}"
        resp = requests.get(link, allow_redirects=True)
        open(filename, "wb").write(resp.content)

    def open_next_window(self):
        if self.current_index < len(self.window_list):
            current_window = self.window_list[self.current_index]
            current_window.show()
            self.current_index += 1

    def on_window_closed(self):
        self.open_next_window()


class TestWindow(QDialog, Ui_TestWindow):
    def __init__(self, imgurl):
        super().__init__()
        self.setupUi(self, imgurl)
        self.save_Button.clicked.connect(self.close)


if __name__ == '__main__':
    user = User()
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())