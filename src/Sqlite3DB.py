import sqlite3
import json


class SQLDB:
    def __init__(self):
        self.con = sqlite3.connect('mountain-info.db')
        self.cur = self.con.cursor()

        with open('Ararat.json', 'r') as f:
            self.data = json.load(f)

        self.cur.execute("DROP TABLE IF EXISTS Ararat")
        self.cur.execute('CREATE TABLE Ararat(ID INT PRIMARY KEY, info TEXT NOT NULL)')

        self.cur.execute("""INSERT INTO Ararat (info) VALUES(?)""", (self.data['info']['Ararat'],))
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
