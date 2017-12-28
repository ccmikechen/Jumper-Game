import sqlite3
import os

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('jumper.db')

    def get_stages(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM stages")
        return c.fetchall()

    def set_stage(self, id, status):
        c = self.conn.cursor()
        c.execute("UPDATE stages SET status = ? WHERE id = ?", (status, id))
        self.conn.commit()

    def get_records(self, stage):
        c = self.conn.cursor()
        c.execute("SELECT * FROM records WHERE stage_id = ? ORDER BY time", (stage,))
        return c.fetchall()

    def add_record(self, stage, time, name):
        c = self.conn.cursor()
        c.execute("INSERT INTO records VALUES (NULL, ?, ?, ?)", (stage, time, name))
        self.conn.commit()

def seed(conn):
    c = conn.cursor()

    c.execute('''
    CREATE TABLE stages
    (id INTEGER PRIMARY KEY, status TEXT)''')

    c.execute("INSERT INTO stages VALUES (1, 'available')")
    c.execute("INSERT INTO stages VALUES (2, 'available')")
    c.execute("INSERT INTO stages VALUES (3, 'locked')")

    c.execute('''
    CREATE TABLE records
    ( id INTEGER PRIMARY KEY,
      stage_id INTEGER,
      time INTEGER,
      player_name TEXT
    )''')

    c.execute("INSERT INTO records VALUES (NULL, 1, 1000, 'test')")

    conn.commit()

def create():
    db = Database()
    try:
        seed(db.conn)
        print("Create database")
    except:
        print("Database is already created")

def drop():
    try:
        os.remove("jumper.db")
    except:
        pass
    print("Drop database")

def reset():
    drop()
    create()
