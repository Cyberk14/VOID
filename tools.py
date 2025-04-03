from youtube_transcript_api import YouTubeTranscriptApi as yta
from youtubesearchpython import VideosSearch
from playwright.sync_api import sync_playwright
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
from typing import Any
import google.generativeai as genai
import requests
import os
import asyncio


os.environ["API_KEY"] = "AIzaSyA8j9C2iflu3S-xFNg0KJfNSjeBpKvpzXY"
genai.configure(api_key=os.environ['API_KEY'])

def knowledge_graph(text: str):
    prompt = f"""extract entities as instances, relationships as predicates in this format:
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
alert: display only list of tuples as they are the only ones needed no additional text needed as plain text.
Now, respond to this text:[{text}], 

response: """
    model = genai.GenerativeModel(model_name='models/gemini-1.5-pro')
    response = model.generate_content(prompt) 
    response.resolve()
    return response.text

class youtube:
    def register(self):
        name = 'Youtube'
        description = '''This is used to retrieve videos from youtube. Examples of how to retrieve data from youtube:
1. Youtube.run("news update for the market") -> searching for news updates for market.
2. Youtube.run("Floods in Argentina") -> when searching for floods in Argentina
3. Youtube.run("Summary of 2022 world cup") -> when searching for 2022 world cup summary'''
        how_to = 'Youtube.run("")'
        
        return {'name': name, 'description': description, 'how to': how_to}
    def run(self, text: str):

        print("searching youtube")
        try:
            links = VideosSearch(text, limit=1).result()
            id, title = links['result'][0]['id'], links['result'][0]['title']
            
            vid = yta.get_transcript(id)
            
            transcript = []
            for text in vid:
                text = text['text']
                transcript.append(text)
                
            transcript = " ".join(transcript)
            
            knowledge = knowledge_graph(transcript)
            
            return knowledge
        
        except Exception as error:
            print(f"An error occurred: {error}")
            
            return error

class search:
    def register(self):
        name = 'Search'
        description = """A tool used to browse the web as a real human would.
# The line `print("searching")` is a print statement in Python that outputs the message
# "searching" to the console. It is used as a way to indicate that the program is
# currently searching for something when the `run` method of the `search` class is
# executed.
Here are som examples of how to run the search tool:
1. Search.run('sentiment on the gold market today') -> when searching for sentiment analysis of the gold market that day.
2. Search.run('When is the date for the us budget reading.') -> when searching for the specific date of the us budget reading."""
        how_to = 'Search.run("")'
        
        return {'name': name, 'description': description, 'how to': how_to}

    def duck_search(self, text: str):
        try:
            print("searching")
            results = DDGS().text(text, region='wt-wt', safesearch='off', timelimit='y', max_results=2)
            
            return results[0]['href'], results[1]['href']
        
        except Exception as error:
            print(f'An error occurred in DDGS: {error}')
            return None
        
    def play_Wright(self, url: str):
        try:
            with sync_playwright() as pw:
                browser = pw.chromium.launch(headless=True)
                context = browser.new_context(viewport={"width": 920, "height": 500})
                page = context.new_page()

                page.goto(url, timeout=0)  # go to URL
                content = page.content()
                
                page.close()
            soup = BeautifulSoup(content, 'html.parser')
            p_tags = soup.find_all('p')
            text = " ".join(tags.get_text() for tags in p_tags)

            return text
        
        except Exception as error:
            print(f'An error occurred in play_wright: {error}')
            return None

    def run(self, text: str):
        if hasattr(asyncio, 'WindowsProactorEventLoopPolicy'):
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
            
            urls = self.duck_search(text)

            knowledge = []

            for url in urls:
                text = self.play_Wright(url)
            
                results = knowledge_graph(' '.join(text))

                knowledge.append(results)

            return knowledge
        
        # except Exception as error:
        #     print('An error occurred when running Search: ', error)
        #     return None
            
ApiKey = "LRUBTT8K83R72KNM"
class AlphaVantage:
    def register(self):
        name = 'AlphaVantage'
        description = "used to fetch ticker data from AlphaVantage Api"
        how_to = 'AlphaVantage.run(ticker: str)'

        return {'name': name, 'description': description, 'how to': how_to}
    
    def run(self, ticker: str):
        self.ticker = ticker
        self.prompt = f"""
This is the data of the ticker: {self.ticker},
OHLCV data: {self.yesterdayData()},
Moving Average Data: {self.MVdata()}"""
        
    
    def yesterdayData(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.ticker}&apikey={ApiKey}'
        r = requests.get(url)
        rawData = r.json()
        return rawData
    
    def MVdata(self): 
        pass
    

