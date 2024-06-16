from typing import List 
import requests
import json

url = 'https://api.jina.ai/v1/embeddings'

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer jina_58f091b726fc400fa28a97ddb9433138j2pVDg8MDJLJUH9jJkC-PkNPh2dh'
}

text = 'Developing intelligent applications quickly requires a deep understanding of both software engineering principles and advanced machine learning techniques By collaborating with a global network of skilled developers data scientists and innovators we can share resources insights and technical expertise This collaborative approach enables us to create cutting-edge solutions that address complex problems and drive technological advancement in various fields fostering innovation and progress'

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

def embeddings(tokens: List[str]):
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

tokens = chunck(text)
print(tokens)
print('--------------------------------------------------------------------------------')
embeddings = embeddings(tokens)
print(embeddings)
