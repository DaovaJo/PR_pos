import sqlite3
from encodings import utf_8

class Stud():
    """РАБОТА С ДАННЫМИ СТУДЕНТА В БД"""
    def __init__(self):
        self.conNect = sqlite3.connect("STUD.db")
        self.cur = self.conNect.cursor()

    def creat_db(self, id, fn, group, state):
        try:
            self.cur.execute("INSERT INTO stud VALUES (?, ?, ?, ?)", (id, fn, group, state))
            self.conNect.commit()
        except:
            self.cur.execute("CREATE TABLE stud(Id, FullName, группа, состояние)")


    





