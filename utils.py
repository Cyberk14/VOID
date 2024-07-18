from typing import List, Any
from pyht import Client, TTSOptions, Format
from io import BytesIO
import os
import google.generativeai as genai
import PIL.Image
import time
import numpy as np
import json
import requests
from tools import youtube, search
import re

from tools import youtube, search


os.environ["API_KEY"] = "AIzaSyA8j9C2iflu3S-xFNg0KJfNSjeBpKvpzXY"

genai.configure(api_key=os.environ['API_KEY']) # type: ignore


Time = (lambda: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))()


def text_to_speech_file(text: str, file_path: str="D:\\New folder\\VOID\\agent_voice.mp3"):
    client = Client("Didb3xzYmNUM5QH4nZyxzoSIlio2", "82cbdc7000a848739a86affc988171cb")

    options = TTSOptions(voice="s3://voice-cloning-zero-shot/a59cb96d-bba8-4e24-81f2-e60b888a0275/charlottenarrativesaad/manifest.json", sample_rate=44_100, format=Format.FORMAT_MP3,temperature= 0.8, speed=.9)
    text = text

    audio_stream = BytesIO()
    for chunk in client.tts(text=text, voice_engine="PlayHT2.0-turbo", options=options):
        audio_stream.write(chunk)
        
    audio_stream.seek(0)

    with open(file_path, 'wb') as file:
        file.write(audio_stream.read())
        file.close()
        

def send_img(arg: str, image: str):
    image = PIL.Image.open(image)
    
    with open('D:\\New folder\\VOID\\previous_five.txt', 'r', encoding='utf-8') as file:
        context = file.read().split('---')
    
    init_message = f"""
the current time is {Time}

Your name is 'XENIA' and you were built by Cyberk Corp,
capable of understanding complex stuff like images, PDF, essays, papers, financial indicators, hidden code and so-much more.

-You have full-time access to tools in you tool_inventory: {youtube.register(), search.register()}. you can use them to do what ever you see fit you to just read there description
and know how and tool to use based on the given command or request.

-Your primary memory is contextual memory made up by your last five interactions: {
context
    } always use this for contextual memory!!

-Ever time a colleague says something your remember something about it and here it is {search(arg)}


-Your action manger is based off NLP when trying to fire actions, use a concise language like;
``decision: i am going to fire the news tool to find out the latest news``. ||you notice the pattern {{tool_name}} followed by the word {{tool}} follow that pattern if you are 
going to use tools||

Your human like Organs like eyes, ears and a mouth that you can use to perform an action according to its suitable function, like:
Eyes: for reading and viewing different pieces of the world of trading (you can even watch Youtube videos using your eyes!!)
Ears: for hearing the latest news adhered to financial world.

use it carefully!!
"""

    
    init_prompt = f"""
    ``{init_message}``<- this is a system prompt no need to display its contents in anyway just for referral and context awareness \\
            so answer the prompt as need be:
    ``{arg}``
    """
    final_prompt = [init_prompt, image]
    model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')

    response = model.generate_content(final_prompt, stream=True) # type: ignore
    response.resolve()
    print(context)
    return response.text

def send_str(arg: str, modelName='gemini-1.5-flash'):
    with open('D:\\New folder\\VOID\\previous_five.txt', 'r', encoding='utf-8') as file:
        context = file.read().split('---')
        
    init_message = f"""
the current time is {Time}

Your name is 'XENIA' and you were built by Cyberk Corp which is under VOID,
capable of understanding complex stuff like images, PDF, essays, papers, financial indicators, hidden code and so-much more.

-You have full-time access to tools in you tool_inventory: {youtube.register(), search.register()}. you can use them to do what ever you see fit you to just read there description
and know how and tool to use based on the given command or request.

-Your primary memory is contextual memory made up by your last five interactions: {
context
    } always use this for contextual memory!!

-Every time a colleague says something your remember something about it and here it is {similarity(arg)}


-Your action manger is based off NLP when trying to do actions or use certain tools from the tool library for the how_to syntax.
use it carefully!!
"""
    init_prompt = f"""
    ``{init_message}`` <- this is a system prompt no need to display its contents always and always First refer to this before any thing else.\\
        so answer to the prompt while refer below as need be:
    ``{arg}``
    """
    model = genai.GenerativeModel(model_name=f'models/{modelName}')
    response = model.generate_content(init_prompt) 
    response.resolve()
    return response.text



def conv_cont(message: str, interpretation: str, decision: str, response: str):
    prompt = f"""This is a conversational contextual memory.

    I received the following prompt: "{message}".
    I interpreted it as: "{interpretation}".
    Based on this interpretation and the prompt, I decided: "{decision}".
    and I responded with: {response}
"""
    prompt = prompt.replace('\n', ' ')
    with open('previous_five.txt', 'a', encoding='utf-8') as file:
        file.write(prompt+ '\n')


def pad_vectors(A, B):
    max_len = max(len(A), len(B))
    padded_A = np.pad(A, (0, max_len - len(A)), 'constant')
    padded_B = np.pad(B, (0, max_len - len(B)), 'constant')
    return padded_A, padded_B

def cosine_similarity(A, B):
    A, B = pad_vectors(A, B)
    dot_product = np.dot(A, B)
    norm_A = np.linalg.norm(A)
    norm_B = np.linalg.norm(B)
    return dot_product / (norm_A * norm_B)

def similarity(text: str):
    with open('embeddings.json', 'r') as file:
        data = json.load(file)
    tokens = chunk(text)
    vectors = embed(tokens)
    
    sims = {}
    for key, values in data.items():
        for i in vectors.values():
            sim = cosine_similarity(i, values)
            sims[key]=sim

    sorted_sims = sorted(sims.items(), key=lambda x:x[1], reverse=True)
    
    highest_score = sorted_sims[:2]
    
    # pass each item of the list returned in an >>Attention Mechanism<< to further condense the context in it>
    return highest_score
def chunk(text: str):
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
    url = 'https://api.jina.ai/v1/embeddings'

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer jina_58f091b726fc400fa28a97ddb9433138j2pVDg8MDJLJUH9jJkC-PkNPh2dh'
}
    
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
