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
    ans = c.execute(f"SELECT password, admin, id FROM Users WHERE username = '{username}'").fetchall()
    if not len(ans):
        return "false"
    if password == ans[0][0]:
        return (ans[0][1], ans[0][2])
    return "false"


def get_tests():
    con = sqlite3.connect("database.db")
    c = con.cursor()
    ans = c.execute("SELECT id, Name FROM Tests").fetchall()
    con.close()
    return ans


def get_test(test_id: int):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    ans = c.execute(f"SELECT imgUrl FROM Vopros WHERE id_test = '{test_id}'").fetchall()
    lst_otv = c.execute(f"SELECT otv FROM Tests WHERE id = '{test_id}'").fetchall()[0][0]
    con.close()
    return (ans, lst_otv)


def create_test(name: str, lst: list, otv: list):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    if not len(c.execute(f"SELECT Name FROM Tests WHERE Name = '{name}'").fetchall()):
        c.execute(f"INSERT INTO Tests(Name, otv) VALUES('{name}', '{'%%%'.join(otv)}')")
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


def create_rez(id_test: int, id_user: int, rez: list):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute(f"INSERT INTO Results(id_test, id_user, rez) VALUES('{id_test}', '{id_user}', '{'%%%'.join(rez)}')")
    con.commit()
    con.close()


def delete_test(id_test: int):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute(f"DELETE FROM Tests WHERE id = '{id_test}'")
    c.execute(f"DELETE FROM Vopros WHERE id_test = '{id_test}'")
    c.execute(f"DELETE FROM Results WHERE id_test = '{id_test}'")
    con.commit()
    con.close()


def get_rez_for_test(test_id: int):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    ans = c.execute(f"SELECT id_user, rez FROM Results WHERE id_test = '{test_id}'").fetchall()
    return ans


def get_users():
    con = sqlite3.connect("database.db")
    c = con.cursor()
    ans = c.execute("SELECT id, username FROM Users").fetchall()
    return ans


def delete_user(user_id: int):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    c.execute(f"DELETE FROM Users WHERE id = '{user_id}'")
    c.execute(f"DELETE FROM Results WHERE id_user = '{user_id}'")
    con.commit()
    con.close()


def get_user_rez(user_id: int):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    ans = c.execute(f"SELECT id_user, rez FROM Results WHERE id_user = '{user_id}'").fetchall()
    return ans