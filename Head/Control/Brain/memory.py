# this will be used to store info that will be used in the future like dates times or more important info 
# that including certain skills and ways of doing a thing ie "learning". 

import sqlite3 as sq
import tools

# long term Memory database.
conn = sq.connect('memory.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS context(Token TEXT NOT NULL, Vector TEXT NOT NULL)""")

def add_mem_db(knowledge) -> None:
    token = chunk()
    vector = embed()

    cursor.execute('INSERT INTO MemoryTable (Token, Vector) VALUES (?, ?)', (token, vector))
    conn.commit()
    conn.close()
    print("DataBase updated successfully!")

def long_term_mem(text, switch: bool = False):
    if not switch:
        return None

    knowledge = tools.knowledge_graph(text)


def index(text: any) -> None:
    with open('previuos-five.txt', r)

    