import sqlite3 as sql
from Typing import Lists, Dict, Any


conn = sql.connect("collected.db")
cus = conn.cursor()

table = cus.execute("""CREATE TABLE IF NOT EXISTS collected (
        name text NOT NULL,
        Email TEXT NOT NULL,
        Phone TEXT NOT NULL
    );""")

class DataBase:
    def __init__(self, **kwargs) -> Any:
        for keys, values in kwargs:
            dict[keys] = values
            
            