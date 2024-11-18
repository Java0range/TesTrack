import sqlite3


def create_user(username: str, password: str, admin=False):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    if not len(c.execute(f"SELECT username FROM Users WHERE username = '{username}'").fetchall()):
        c.execute(f"INSERT INTO Users(username, password, admin) VALUES( '{username}', '{password}', '{admin}' )")
        con.commit()
    con.close()
    raise Exception


def auth(username: str, password: str):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    ans = c.execute(f"SELECT password, admin FROM Users WHERE username = '{username}'").fetchall()[0]
    if password == ans[0]:
        return ans[1]
    return "false"


def get_tests():
    con = sqlite3.connect("database.db")
    c = con.cursor()
    ans = c.execute("SELECT * FROM Tests").fetchall()
    con.close()
    return ans


def get_test(test_id: int):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    ans = c.execute(f"SELECT imgUrl FROM Vopros WHERE id_test = '{test_id}'").fetchall()
    con.close()
    return ans


def create_test(name: str, lst: list):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    if not len(c.execute(f"SELECT Name FROM Tests WHERE Name = '{name}'").fetchall()):
        c.execute(f"INSERT INTO Tests(Name) VALUES('{name}')")
        con.commit()
        con.close()
        con = sqlite3.connect("database.db")
        c = con.cursor()
        test_id = c.execute(f"SELECT id FROM Tests WHERE Name = '{name}'").fetchall()[0][0]
        for item in lst:
            c.execute(f"INSERT INTO Vopros(id_test, imgUrl) VALUES('{test_id}', '{item}')")
        con.commit()
        con.close()
        return "true"
    return "error"


def create_rez(id_test: str, id_user: str, rez: list):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute(f"INSERT INTO Results(id_test, id_user, rez) VALUES('{id_test}', '{id_user}', '{rez}')")


create_rez("1", "1", [1, 2])