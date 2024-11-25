from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QFileDialog
from PyQt6 import QtGui, QtWidgets
from ConnectWindow import Ui_ConnectServer
from TestList import Ui_TestList
from TestWindow import Ui_TestWindow
from RezWindow import Ui_Rez_Window
from AuthAdmin import Ui_AuthWindow
from AdminPanel import Ui_AdminPanel
from AdminTestList import Ui_AdminTestList
from AdminCreateTest1 import Ui_create_test_1
from AdminCreateTest2 import Ui_create_test_2
from AdminTestsList import Ui_AdminTestsList
from AdminUsersList import Ui_AdminUsersList
from PyQt6.QtWidgets import QMessageBox
import sys
import requests


class User:
    def __init__(self):
        self.link = "http://127.0.0.1:8000"
        self.admin = False
        self.test_id = 1
        self.user_id = 0
        self.test_window = 0
        self.ans = []
        self.otvets = []

    def edit_admin(self, lvl):
        self.admin = lvl

    def edit_test_id(self, id):
        self.test_id = id


class InfoTest:
    def __init__(self):
        self.count_vopros = 0
        self.test_name = ""
        self.img_url = {}

    def get_list(self):
        return self.img_url.values()



class MainWindow(QMainWindow, Ui_ConnectServer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.pushButton.clicked.connect(self.auth)
        self.actionAdmin_Panel.triggered.connect(lambda: self.action_clicked(self.actionAdmin_Panel.text()))
        self.actionServer_Settings.triggered.connect(lambda: self.action_clicked(self.actionServer_Settings.text()))

    def auth(self):
        try:
            name = self.lineEdit_3.text()
            password = self.lineEdit.text()
            link = f"{user.link}/users/auth/"

            data = {
                "username": name,
                "password": password
            }
            responce = requests.post(link, json=data)
            user.edit_admin(True if responce.json()["admin"] else False)
            user.user_id = int(responce.json()["id"])
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
        except Exception:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
            msg_box.exec()

    def action_clicked(self, event):
        match event:
            case "Admin Panel":
                self.admin_auth = AuthAdmin()
                self.admin_auth.show()


class TestList(QDialog, Ui_TestList):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 500)
        self.pushButton_2.clicked.connect(self.test_clicked)
        try:
            link = f"{user.link}/tests/tests/"
            responce = requests.get(link).json()["msg"]
            for i in responce:
                numRows = self.tableWidget.rowCount()
                self.tableWidget.insertRow(numRows)
                self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(i[1]))
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
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
            responce = requests.post(link, json=data).json()
            user.otvets = responce["otv"].split("%%%")
            responce = responce["msg"]
            for i in responce:
                self.save_img(i[0])
            self.window_list = []
            for title in responce:
                window = TestWindow(f"./src/temp/{title[0]}")
                window.closed.connect(self.on_window_closed)
                self.window_list.append(window)
            rez_window = RezWindow()
            self.window_list.append(rez_window)
            if len(self.window_list) > 0:
                self.current_index = 0
                self.open_next_window()
            self.main.testlist.close()

        except Exception:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
            msg_box.exec()

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
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.save_Button.clicked.connect(self.close)

    def closeEvent(self, event):
        user.ans.append(self.otvet_input.text() if self.otvet_input.text() else "None")
        self.closed.emit()
        event.accept()


class RezWindow(QDialog, Ui_Rez_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.tableWidget.setColumnWidth(1, 275)
        self.tableWidget.setColumnWidth(2, 275)

    def show(self):
        for i in range(len(user.ans)):
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(user.ans[i]))
            self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(user.otvets[i]))
        rez = []
        for i in range(len(user.ans)):
            if user.ans[i] == user.otvets[i]:
                rez.append("1")
            else:
                rez.append("0")
        link = f"{user.link}/tests/saverez/"
        data = {
            "test_id": user.test_id,
            "user_id": user.user_id,
            "rez": rez
        }
        responce = requests.post(link, json=data).json()
        super().show()


class AuthAdmin(QDialog, Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.login_button.clicked.connect(self.auth)

    def auth(self):
        try:
            name = self.server_inp.text()
            password = self.key_inp.text()
            link = f"{user.link}/users/auth/"

            data = {
                "username": name,
                "password": password
            }
            responce = requests.post(link, json=data)
            match responce.json()["admin"]:
                case "True":
                    self.panel = AdminPanel()
                    self.panel.show()
                    self.close()
                case "False":
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Icon.Critical)
                    msg_box.setText("Ошибка")
                    msg_box.setWindowTitle("Ошибка")
                    msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
                    msg_box.exec()
        except Exception:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
            msg_box.exec()


class AdminPanel(QDialog, Ui_AdminPanel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.pushButton_2.clicked.connect(self.tests_button)
        self.pushButton.clicked.connect(self.users_button)

    def tests_button(self):
        self.tests_window = AdminTestsList()
        self.tests_window.show()
        self.close()

    def users_button(self):
        self.users_window = AdminUsersList()
        self.users_window.show()
        self.close()


class AdminTestsList(QDialog, Ui_AdminTestsList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 500)
        self.pushButton_4.clicked.connect(self.reload)
        self.pushButton_2.clicked.connect(self.create_test)
        self.pushButton_5.clicked.connect(self.delete_test)
        self.pushButton_3.clicked.connect(self.open_test)
        try:
            link = f"{user.link}/tests/tests/"
            responce = requests.get(link).json()["msg"]
            for i in responce:
                numRows = self.tableWidget.rowCount()
                self.tableWidget.insertRow(numRows)
                self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(i[1]))
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
            msg_box.exec()

    def reload(self):
        self.tableWidget.setRowCount(0)
        try:
            link = f"{user.link}/tests/tests/"
            responce = requests.get(link).json()["msg"]
            for i in responce:
                numRows = self.tableWidget.rowCount()
                self.tableWidget.insertRow(numRows)
                self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(i[1]))
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
            msg_box.exec()

    def create_test(self):
        self.create_test_window = CreateTest1()
        self.create_test_window.show()

    def delete_test(self):
        try:
            row = self.tableWidget.currentRow()
            test_id = int(self.tableWidget.item(row, 0).text())
            link = f"{user.link}/admin/deletetest/"
            data = {
                "test_id": test_id
            }
            requests.delete(link, json=data)
        except Exception:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
            msg_box.exec()

    def open_test(self):
        try:
            row = self.tableWidget.currentRow()
            test_id = int(self.tableWidget.item(row, 0).text())
            link = f"{user.link}/tests/reztest/"
            data = {
                "test_id": test_id
            }
            ans = requests.post(link, json=data).json()["msg"]
            if ans != "error":
                self.admin_test_list = AdminTestList(ans)
                self.admin_test_list.show()
        except Exception:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
            msg_box.exec()



class CreateTest1(QDialog, Ui_create_test_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.pushButton.clicked.connect(self.next)

    def next(self):
        infotest.count_vopros = self.lineEdit_3.text()
        infotest.test_name = self.lineEdit_2.text()
        self.create_test_window_2 = CreateTest2()
        self.create_test_window_2.show()
        self.close()


class CreateTest2(QDialog, Ui_create_test_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.tableWidget.setColumnWidth(0, 180)
        self.tableWidget.setColumnWidth(1, 180)
        self.pushButton.clicked.connect(self.create_test)
        for i in range(int(infotest.count_vopros)):
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            button = QPushButton(f"Open_{i}")
            self.tableWidget.setCellWidget(i, 0, button)
            button.clicked.connect(self.open_img)
            self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(i))
            self.tableWidget.setRowHeight(i, 40)
        self.tableWidget.setRowCount(int(infotest.count_vopros))

    def open_img(self):
        key = self.sender().text().split("_")[1]
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        infotest.img_url[key] = file_name

    def create_test(self):
        try:
            otvets = []
            for j in range(int(infotest.count_vopros)):
                otvets.append(self.tableWidget.item(j, 1).text())
            img_lst = []
            for i in infotest.img_url.values():
                link = f"{user.link}/files/upload"

                files = {
                    "upload_file": open(i, "rb")
                }
                resp = requests.post(link, files=files).json()["msg"]
                img_lst.append(resp)
            link = f"{user.link}/admin/createtest/"
            data = {
                "name": infotest.test_name,
                "imgUrls": img_lst,
                "otv": otvets
            }
            requests.post(link, json=data)
            self.close()
        except Exception:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText("Ошибка")
            msg_box.setWindowTitle("Ошибка")
            msg_box.setWindowIcon(QtGui.QIcon("./src/icon.png"))
            msg_box.exec()


class AdminTestList(QDialog, Ui_AdminTestList):
    def __init__(self, lst: list):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 500)
        for i in lst:
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(" ".join(i[1].split("%%%"))))


class AdminUsersList(QDialog, Ui_AdminUsersList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./src/icon.png"))
        

if __name__ == '__main__':
    user = User()
    infotest = InfoTest()
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())