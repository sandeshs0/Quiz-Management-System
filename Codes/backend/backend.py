import sqlite3
def connect():
    conn= sqlite3.connect("Quizproject.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE Create_Quiz (id INTEGER PRIMARY KEY, Subject Name TEXT, Questions Text TEXT, Option1 TEXT, Option2 TEXT, Option3 TEXT, Option4  TEXT, Answer TEXT")
    conn.commit()
    conn.close()



 