from youtube_transcript_api import YouTubeTranscriptApi as yta
from youtubesearchpython import VideosSearch
from playwright.sync_api import sync_playwright
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
from typing import Any
import requests
import os

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

            
            video = {'title': title, 'content': transcript}
            return video
        
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

    def run(self, text: str):
        import time
        try:
            # The line `print("searching")` is a print statement in Python that outputs the message
            # "searching" to the console. It is used as a visual indicator to show that the program is
            # currently searching for something.
            print("searching")
            results = DDGS().text(text, region='wt-wt', safesearch='off', timelimit='y', max_results=1)[0]['href']
            
            time.sleep(4)
            print(results)
            with sync_playwright() as pw:
                browser = pw.chromium.launch(headless=False)
                context = browser.new_context(viewport={"width": 920, "height": 500})
                page = context.new_page()

                page.goto(results, timeout=0)  # go to url
                content = page.content()
                soup = BeautifulSoup(content, 'html.parser')
                page.close()

            p_tags = soup.find_all('p')
            
            return p_tags
        except Exception as error:
            print('An error occurred when running Search: ', error)
            
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
    

