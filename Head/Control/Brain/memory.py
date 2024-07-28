# this will be used to store info that will be used in the future like dates times or more important info 
# that including certain skills and ways of doing a thing ie "learning". 

import sqlite3 as sq
import utils

# long term Memory database.
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


def long_term_mem(switch: bool = False):
    if not switch:
        return None

    prompt = f"""extract entities as instances, relationships as predicates in this format:
(inst(entity1), predicate(relation), inst(entity2))
for example:
[ 
    ("Retail traders", "are in", "long positions"),
    ("Retail traders", "are in", "short positions"),
    ("Short positions", "ratio of", "1.01 to 1, short-to-long"),
    ("Long positions", "decreased by", "13.24% since yesterday"),
    ("Long positions", "decreased by", "13.73% over the past week"),
    ("Short positions", "increased by", "8.36% daily"),
    ("Short positions", "increased by", "6.44% weekly"),
    ("Net-short positioning", "implies potential for", "Gold price appreciation"),
    ("Short bias", "strengthens", "contrarian bullish view on Gold"),
    ("Retail traders", "are net-long", "US Crude Oil"),
    ("Long positions", "outweigh", "short positions, 1.40 to 1"),
    ("Net-long traders", "decreased by", "0.43% daily"),
    ("Net-long traders", "increased by", "7.19% weekly"),
    ("Net-short traders", "grown by", "4.31% since yesterday"),
    ("Net-short traders", "declined by", "14.98% over the week"),
    ("Net-long majority", "implies potential for", "US Crude price decreases"),
    ("Short-term and medium-term changes", "yield ambiguous outlook for", "Oil - US Crude"),
    ("Retail trader data", "reveals", "bearish tilt, S&P 500"),
    ("Net-long traders", "grown by", "13.58% since yesterday"),
    ("Net-long traders", "grown by", "6.75% over the week"),
    ("Net-short traders", "declined by", "8.07% daily"),
    ("Net-short traders", "declined by", "2.91% weekly"),
    ("Dominant net-short sentiment", "suggests continued", "US 500 price appreciation"),
    ("Decline in net-short positions", "indicates possible reversal in", "current US 500 uptrend"),
    ("DailyFX", "provides", "forex news and technical analysis"),
    ("Nick Cawley", "contact via", "Twitter @nickcawley1")
]

Now, respond to this text:[{text}], response:"""

    response = utils.send_str(prompt)
    
    return response

def update(switch:bool=False):
    if switch:
        with open('D:/New folder/VOID/previous_five.txt', 'r', encoding='utf-8') as file:
            cont_memory = file.readlines()
            
        if len(cont_memory) > 5:
            cont_memory.remove(cont_memory[0])
        with open('D:\\New folder\\VOID\\previous_five.txt', 'w', encoding='utf-8') as file:
            for line in cont_memory:
                file.write(line)
    return None

