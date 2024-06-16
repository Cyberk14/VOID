# this will be used to store info that will be used in the future like dates times or more important info 
# that including certain skills and ways of doing a thing ie "learning". 

from brain import Brain, send_str
import sqlite3 as sq
from typing import List
from Head.Input.eyes import see
import requests
import json

text  =

url = 'https://api.jina.ai/v1/embeddings'

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer jina_58f091b726fc400fa28a97ddb9433138j2pVDg8MDJLJUH9jJkC-PkNPh2dh'
}


# contextual Memory database.
conn = sq.connect('memory.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS context(Token , Vector)""")

def trash_memory():
    prompt = f'''
    your Brain would want ``trash some`` of its Memory: >>>{memory_to_trash}<<< to save some space but before it does so. Can you summarize and compress it to a small but still in an understandable format/way.
    '''
    
    memory_sum = send_str(prompt)
    return memory_sum

def chunck(text: str = text):
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

def add_mem_db():
    tokens = chunck()
    vectors = embed(tokens)
    
    tokens = vectors.keys()
    vectors = vectors.values()
    
    for token, vector in zip(tokens, vectors): # type: ignore
        cursor.execute('INSERT INTO TABLE (Token, Vector)  VALUES (?, ?)',(token, vector)) # type: ignore
        conn.commit()
    
    conn.close()
    print("DataBase updated successfully!")

