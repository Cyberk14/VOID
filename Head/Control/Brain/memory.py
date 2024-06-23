# this will be used to store info that will be used in the future like dates times or more important info 
# that including certain skills and ways of doing a thing ie "learning". 

import sqlite3 as sq
from typing import List
import utils
import requests


url = 'https://api.jina.ai/v1/embeddings'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer jina_58f091b726fc400fa28a97ddb9433138j2pVDg8MDJLJUH9jJkC-PkNPh2dh'
}


# contextual Memory database.
conn = sq.connect('memory.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS context(Token TEXT NOT NULL, Vector TEXT NOT NULL)""")

def chunck(text: str):
    sent = text.split(' ')

    tokens = []
    epoch = 20
    start = 0

    while start < len(sent):
        s = sent[start:start + epoch]
        tokens.append(' '.join(s))
        start += epoch
        
    return tokens

def embed(tokens: List[str]):
    vectors = {}
    
    for token in tokens:
        data = {
    'input': token,
    'model': 'jina-embeddings-v2-base-en',
    'encoding_type': 'float'
    }
        response = requests.post(url, headers=headers, json=data).json()
        embedding = response['data'][0]['embedding']
        
        vectors[token]=embedding

    return vectors

def add_mem_db(vector, token):
    tokens = chunck()
    vector = embed()

    cursor.execute('INSERT INTO MemoryTable (Token, Vector) VALUES (?, ?)', (token, vector))
    conn.commit()
    conn.close()
    print("DataBase updated successfully!")


def previous_5(switch:bool=False):
    if switch:
        with open('D:\\New folder\\VOID\\previous_five.txt', 'r+', encoding='utf-8') as file:
            text = file.read()
            
            previous = text.split('---')
            
        if len(previous) == 5:
            prompt = f"""
            from this piece of text is the contextual memory buffer and its going to br 
            deleted but before its deleted remove only and only the relevant that needs to be 
            stored for future use {previous[0]}, if there no info to be stored return the word 'None'
            """
            response = utils.send_str(prompt)
            if 'none' in response.lower():
                pass
            else:
                with open('D:\\New folder\\VOID\\previous_five.txt', 'w', encoding='utf-8') as file:
                    previous.remove(previous[0])
                    for i in previous:
                        file.write(i)
                    print("upadated and stored")

    return None

