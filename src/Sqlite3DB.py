import sqlite3
import json


class SQL3DB:
    def __init__(self):
        self.con = sqlite3.connect('info.db')
        self.cur = self.con.cursor()

        with open('Ararat.json', 'r') as f:
            self.ararat_data = json.load(f)

        with open('Dishes.json', 'r') as f1:
            self.dishes_data = json.load(f1)

        self.cur.execute("DROP TABLE IF EXISTS StoredInfo")
        self.cur.execute('CREATE TABLE StoredInfo(ID INT PRIMARY KEY, name TEXT NOT NULL, info TEXT NOT NULL)')

        self.cur.execute("""INSERT INTO StoredInfo (info) VALUES(?, ?)""", (self.ararat_data['mountain']['Ararat'], self.dishes_data['dishes'], ))
        self.con.commit()

    def output_ararat(self):
        try:
            out = {'name': 'Ararat', 'info': ''}
            out1 = self.cur.execute('SELECT info FROM Ararat')
            out2 = out1.fetchall()
            for item in out2:
                out['info'] = ''.join(item)
            self.con.close()
            return out
        except:
            return False
