import sqlite3 as sq 
def add_mem_db(vector, token):
    conn = sq.connect('memory.db')
    cursor = conn.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS context(Token , Vector)""")
        
    # tokens = chunck()
    # vectors = embed(tokens)
    
    # tokens = vectors.keys()
    # vectors = vectors.values()
    
    
    
    # for token, vector in zip(tokens, vectors): # type: ignore
    cursor.execute('INSERT INTO TABLE context(Token, Vector)  VALUES (?, ?)',(token, vector)) # type: ignore
    conn.commit()
    
    conn.close()
    print("DataBase updated successfully!")

add_mem_db('i fuck you', [0.3, .5, -.4])
