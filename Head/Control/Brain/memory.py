# this will be used to store info that will be used in the future like dates times or more important info 
# that including certain skills and ways of doing a thing ie "learning". 

from brain import Brain, send_str
import sqlite3 as sq

# contextual Memory database.
conn = sq.connect('memory.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS context()""")

def trash_memory():
    prompt = f'''
    your Brain would want ``trash some`` of its Memory: >>>{memory_to_trash}<<< to save some space but before it does so. Can you summarize and compress it to a small but still in an understandable format/way.
    '''
    
    memory_sum = send_str(prompt)
    return memory_sum

def embed(data: str):
    return data

def chuncker():
    
tokens = []
epoch = 20
s_epoch = 20
start = 0
for s in sent:
    s = sent[start:epoch]
    if not s:
        s = sent[epoch-s_epoch:]
    tokens.append(s)
    start+=epoch
    epoch+=s_epoch
    
    if len(s) == 0:
        break
    tokens.pop()
    
    return tokens
    
