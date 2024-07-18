# this will be used to store info that will be used in the future like dates times or more important info 
# that including certain skills and ways of doing a thing ie "learning". 

import sqlite3 as sq
from typing import List
import utils
import requests
import numpy as np




# contextual Memory database.
conn = sq.connect('memory.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS context(Token TEXT NOT NULL, Vector TEXT NOT NULL)""")



def add_mem_db(vector, token):
    tokens = chunk()
    vector = embed()

    cursor.execute('INSERT INTO MemoryTable (Token, Vector) VALUES (?, ?)', (token, vector))
    conn.commit()
    conn.close()
    print("DataBase updated successfully!")


def update(switch:bool=False):
    if switch:
        with open('D:/New folder/VOID/previous_five.txt', 'r') as file:
            cont_memory = file.readlines()
            
        if len(cont_memory) > 5:
            cont_memory.remove(cont_memory[0])
        with open('D:\\New folder\\VOID\\previous_five.txt', 'w') as file:
            for line in cont_memory:
                file.write(line)
    return None

