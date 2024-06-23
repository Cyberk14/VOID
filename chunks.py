
from typing import List 
import requests
import json

url = 'https://api.jina.ai/v1/embeddings'

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer jina_58f091b726fc400fa28a97ddb9433138j2pVDg8MDJLJUH9jJkC-PkNPh2dh'
}

def chunk(text: str):
    sent = text.split(' ')
    print(len(sent))
    tokens = []
    epoch = 20
    start = 0

    while start < len(sent):
        if start > 0:
          s = sent[start-6:start + epoch]
          tokens.append(' '.join(s))
          start += epoch
          print(len(s))
        elif start == 0:
          s = sent[start:start + epoch]
          tokens.append(' '.join(s))
          start += epoch
          print(len(s))
    print(len(tokens))
    return tokens

# def embed(tokens: List[str]):
#     vectors = {}
    
#     for token in tokens:
#       data = {
#   'input': token,
#   'model': 'jina-embeddings-v2-base-en',
#   'encoding_type': 'float'
# }
#       response = requests.post(url, headers=headers, json=data).json()
#       print(response)
#       embedding = response['data'][0]['embedding']
      
#       vectors[token]=embedding

#     return vectors
  
# tokens = chunck(text)
# vectors = embed(tokens)

# with open('embeddings.json', 'w+') as file:
#   json.dump(vectors, file)
#   file.close()


def KG(text: str ):
  prompt = f'''Input:
heres is the text for you to process:
{text}

Output:

A list of dictionaries, where each dictionary represents a relation between two entities. Each dictionary should have the following keys:
node1: The first entity (string format)
node2: The second entity (string format)
relation: The relation between node1 and node2 (string format)
Instructions:

Identify and extract all mentions of entities in the text. Entities can be of various formats, including:

People (e.g., Albert Einstein, Barack Obama)
Organizations (e.g., Google, United Nations)
Locations (e.g., New York City, Mount Everest)
Dates (e.g., 14th July, 2023)
Numbers (e.g., 3.14, 100)
Quantities (e.g., 5 meters, 2 gallons)
Other custom entity types relevant to your domain (specify these if applicable)
Analyze the relationships between the identified entities. Look for verbs, prepositions, conjunctions, or other grammatical clues that indicate how the entities are connected.

For each relation you find, create a dictionary with the following structure:

node1: The first entity involved in the relation.
node2: The second entity involved in the relation.
relation: The type of relation between node1 and node2. Use a clear and concise verb or phrase to describe the connection (e.g., "founded", "located in", "discovered").
Include all possible relations, even if they seem ambiguous or uncertain. The LLM can output a confidence score (optional) to indicate the certainty of each relation.

Example:

Input:

"Albert Einstein, a brilliant physicist, developed the theory of relativity in 1905. He received the Nobel Prize in Physics in 1921."

Output:

[
  {{
    "node1": "Albert Einstein",
    "node2": "theory of relativity",
    "relation": "developed"
  }},
  {{
    "node1": "Albert Einstein",
    "node2": "Nobel Prize in Physics",
    "relation": "received"
  }},
  {{
    "node1": "theory of relativity",
    "node2": "1905",
    "relation": "developed in" (or "published in")
  }},
  {{
    "node1": "Nobel Prize in Physics",
    "node2": "1921",
    "relation": "awarded in"
  }}
] 
  '''
  # response = send_str(prompt)
  
  # print(response)
  
  # time.sleep(5)
  # return response


# if __name__ == '__main__':
  # with open('D:\\New folder\\VOID\\Head\\Input\\tesla_10k_2023.txt', 'r') as file:
  #   text = file.read()
  # text = chunck(text)
  
  # print(text)
