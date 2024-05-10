import sqlite3 as sql
# import embedder using the google embedders.

# import raw_data deactivate

def database():
    conn = sql.connect("remoteMemory")
    c = conn.cursor()
    
    c
    
class Memory:
    # retrives data to turn it into workable chunks.
    def get_memory(self, raw_data):
        self.rawData = raw_data

    def storeData(self, dataBase):
        pass

class ShortermMemory(Memory):
    def update(self):
        pass

class LongtermMemory(Memory):
    def update(self):
        pass
        

        
            

