import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self._init_tables

    def _init_tables(self):
        pass
