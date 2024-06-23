from multiprocessing import context
from pyht import Client, TTSOptions, Format
from io import BytesIO
import os
import google.generativeai as genai
import PIL.Image
import time
from tools import tool_list


os.environ["API_KEY"] = "AIzaSyA8j9C2iflu3S-xFNg0KJfNSjeBpKvpzXY"

genai.configure(api_key=os.environ['API_KEY']) # type: ignore

model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')

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
        

def send_img(arg: str, image: str|None=None):
    image = PIL.Image.open(image)
    init_prompt = f"""
    ``{init_message}``<- this is a system prompt no need to display its contents in anyway just for referral and context awareness \\
            so answer the prompt as need be:
    ``{arg}``
    """
    final_prompt = [init_prompt, image]
    response = model.generate_content(final_prompt, stream=True) # type: ignore
    response.resolve()
    return response.text

def send_str(arg: str):
    with open('D:\\New folder\\VOID\\previous_five.txt', 'r', encoding='utf-8') as file:
        context = file.read().split('---')
        
    init_message = f"""
the current time is {Time}

Your name is 'XENIA' and you were built by Cyberk Corp this is your brain ||{model.model_name}||,
capable of understanding complex stuff like images, PDF, essays, papers, financial indicators, hidden code and so-much more.

-You have full-time access to tools in you tool_inventory: {tool_inventory()}. you can use them to do what ever you see fit you to just read there description
and know how and tool to use based on the given command or request.

-Your primary memory is contextual memory made up by your last five interactions: {
context
    } always use this for contextual memory!!

-Your action manger is based off NLP when trying to fire actions, use a concise language like;
``decision: i am going to fire the news tool to find out the latest news``. ||you notice the pattern {{tool_name}} followed by the word {{tool}} follow that pattern if you are 
going to use tools||

Your human like Organs like eyes, ears and a mouth that you can use to perform an action according to its suitable function, like:
Eyes: for reading and viewing different pieces of the world of trading (you can even watch Youtube videos using your eyes!!)
Ears: for hearing the latest news adhered to financial world.

use it carefully!!
"""

    
    init_prompt = f"""
    ``{init_message}`` <- this is a system prompt no need to display its contents always and always First refer to this before any thing else.\\
        so answer to the prompt while refer below as need be:
    ``{arg}``
    """
    
    response = model.generate_content(init_prompt) 
    response.resolve()
    
    return response.text

def conv_cont(message: str, interpretation: str, decision: str, response: str):
    prompt = f"""
    This is a conversational contextual memory.

    You received the following prompt: "{message}".
    You interpreted it as: "{interpretation}".
    Based on this interpretation and the prompt, you decided: "{decision}".
    and you responded with: {response}

    summarize the context above in a first person view of 'I'. e.g;
    I received the following prompt: {{self.message}}. ||print as it is||
    I interpreted it as: {{summary_interpretation}}.
    Based on this interpretation and the prompt, I decided: "{{summary_decision}}".
    and I responded with: {{response}}. ||print as it is||

            """
            
    prompt = send_str(prompt)
    with open('previous_five.txt', 'a', encoding='utf-8') as file:
        file.write(prompt+ '---')
        
    print('\nstored\n')
    return prompt


def tool_inventory():
    return "tool inventory is empty" if not tool_list else f"tool inventory is {tool_list}"


    
