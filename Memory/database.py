import json
import collected
# import embedder using the google embedders.

# import raw_data deactivate

def embedder():
    pass

def database():
    embeddings = embedder()
    data = collected
    
    dict = {}
    for x, y in data, embeddings:
        dict[x]= y
        
    with open("jsonData.json", "w+") as jsonData:
        jsonData.write(jsonData.dumps(dict))
        jsonData.close()
        
        
    
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
        

        
            

