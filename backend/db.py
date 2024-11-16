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