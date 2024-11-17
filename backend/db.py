import sqlite3


def create_user(username, password, admin=False):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    if not len(c.execute(f"SELECT username FROM Users WHERE username = '{username}'").fetchall()):
        c.execute(f"INSERT INTO Users(username, password, admin) VALUES( '{username}', '{password}', '{admin}' )")
        con.commit()
    con.close()
    raise Exception


def auth(username, password):
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
    ans = c.execute(f"SELECT id, imgUrl FROM Vopros WHERE id = '{test_id}'").fetchall()
    con.close()
    return ans


def create_test(name: str, lst: list):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    if not len(c.execute(f"SELECT Name FROM Tests WHERE Name = '{name}'").fetchall()):
        c.execute(f"INSERT INTO Tests(Name) VALUES('{name}')")
        con.commit()
        test_id = c.execute("SELECT id FROM Tests WHERE Name = '{name}'").fetchall()[0]
        for item in lst:
            c.execute(f"INSERT INTO Vopros(id_test, imgUrl) VALUES('{test_id}', '{item}')")
        con.commit()
        con.close()
        return "true"
    return "error"


print(create_test("TestName2", ["1.png", "2.png"]))