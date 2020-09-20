import sqlite3

con = sqlite3.connect('app.db')


def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('''CREATE TABLE APPS (
    APP_NAME VARCHAR
    )''')
    con.commit()
    con.close()


sql_fetch(con)
