
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
from tools import youtube, search, AlphaVantage
import re


os.environ["API_KEY"] = "AIzaSyA8j9C2iflu3S-xFNg0KJfNSjeBpKvpzXY"

genai.configure(api_key=os.environ['API_KEY']) # type: ignore

Youtube, Search, Alpha_vantage = youtube(), search(), AlphaVantage()

Time = (lambda: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))()

def text_to_speech_file(text: str, file_path: str="D:\\New folder\\VOID\\agent_voice.mp3"):
    try:
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
    except Exception as error:
        print(f'An error occurred with audio: {error}')
        return None

def send_img(arg: str, image: str):
    image = PIL.Image.open(image)
    
    with open('D:\\New folder\\VOID\\previous_five.txt', 'r', encoding='utf-8') as file:
        context = file.read().split('---')
    init_message = f"""
the current time is {Time}

Your name is 'XENIA' and you were built by Cyberk Corp which is under VOID,
capable of understanding complex stuff like images, PDF, essays, papers, financial indicators, hidden code and so-much more.

-You have full-time access to tools in you tool_inventory: {Youtube.register(), Search.register(), Alpha_vantage.register()}. you can use them to do what ever you see fit you to just read there description
and know how and tool to use based on the given command or request.

-Your primary memory is contextual memory made up by your last five interactions: {
context
    } always use this for contextual memory!!

-Every time a colleague says something your remember something about it and here it is try:
            
"""
    init_prompt = f"""
    ``{init_message}`` <- this is a system prompt no need to display its contents always and always First refer to this before any thing else.\\
        so answer to the prompt while refer below as need be:
    ``{arg}``
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

-You have full-time access to tools in you tool_inventory: {Youtube.register(), Search.register(), Alpha_vantage.register()}. you can use them to do what ever you see fit you to just read there description
and know how and tool to use based on the given command or request.

-Your primary memory is contextual memory made up by your last five interactions: {
context
    } always use this for contextual memory!!

-Every time a colleague says something your remember something about it and here it is try:
            
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


def action(decision: str):
    tools = Youtube.register()['name'],Search.register()['name']

    pattern = r"(" + "|".join(re.escape(tool) for tool in tools) + r")\.run\(['\"](.*?)['\"]\)"
    
    matches = re.findall(pattern, decision)
    if matches:
        for func, arg in  matches:
            exec(f'result = {func}.run("{arg}")', globals())
            
        return result
    return None

def conv_cont(message: str,  decision: str, response: str):
    conv = f"""This is a conversational contextual memory.
    User ---> {message}, 
    I ---> {response}
"""
    conv = conv.replace('\n', ' ')
    with open('previous_five.txt', 'a', encoding='utf-8') as file:
        file.write(f"{Time} :{conv}")


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

def embed(tokens: Any):
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
