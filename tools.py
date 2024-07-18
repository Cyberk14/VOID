from youtube_transcript_api import YouTubeTranscriptApi as yta
from youtubesearchpython import VideosSearch
from playwright.sync_api import sync_playwright
from typing import Any
import requests
import os



# def tool(func: Any):
#     def wrapper(*args: Any):
#         func_name, desc, how_to = func()
#         tool_list[func_name] = {'description': desc,
#                                 'how to run': how_to}
        
#     return wrapper

class youtube:
    def register(self):
        name = 'Youtube'
        desc = '''This is used to retrieve videos from youtube and view them'''
        how_to = 'youtube.run(text: str)'
        
        return name, desc, how_to
    def run(self, text: str):
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
    
class search:
    def register(self):
        name = 'Search'
        desc = """A tool used to browse the web as a real human would."""
        how_to = 'search.run(query: str)'
        
        return name, desc, how_to
    
    def run(self, query):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 920, "height": 500})
            page = context.new_page()

            page.goto("https://finance.yahoo.com", timeout=0)  # go to url

            content = page.content()
            soup = BeautifulSoup(content, 'html.parser')
            page.close()

        header_element = str(soup.find_all(class_="module-hero hero-3-col svelte-6i0owd"))
        header_element = BeautifulSoup(header_element, 'html.parser')

        a_tags = header_element.find_all('a')
        scrape = []

        for tag in a_tags:
            title = tag.get('title')
            href = tag.get('href')
            
            scrape.append({title: href})
            print({title: href})
            

        # Remove duplicates
        unique_data = []
        seen_items = set()
        for item in scrape:
            for key, value in item.items():
                if (key, value) not in seen_items:
                    seen_items.add((key, value))
                    unique_data.append(item)

ApiKey = "LRUBTT8K83R72KNM"
class AlphaVantage:
    def register(self):
        name = 'AlphaVantage'
        desc = "used to fetch ticker data from AlphaVantage Api"
        how_to = 'AlphaVantage.run(ticker: str)'

        return name, desc, how_to
    def run(self, ticker):
        self.ticker = ticker
        self.prompt = f"""
            You are a market trend detective! Your mission is to analyze the provided historical market data (OHLCV format) and crack the case of the current and potential future trends.

Sharpen your tools:

Moving Averages: {self.MVdata()} Calculate SMAs for various periods (e.g., 50-day, 200-day) and compare price action to identify uptrends, downtrends, or sideways movement.
Support & Resistance: Look for historical price action patterns to pinpoint support and resistance levels. Uptrends break above resistance, downtrends break below support, and sideways movement bounces between those levels.
Volume Analysis: Watch how trading volume interacts with price movements. Increasing volume on upticks and decreasing volume on pullbacks suggest uptrends. The opposite suggests downtrends, with a caveat for potential bear traps. Sideways movement often has consistent volume.
Bonus Tools: Consider technical indicators like RSI and MACD for additional confirmation.
Present your findings:

Classify the current trend (uptrend, downtrend, sideways).
Explain your reasoning based on the evidence gathered from moving averages, support & resistance, and volume analysis.
Briefly discuss the possibility of a trend reversal based on the current market conditions.
Remember:

Technical analysis has limitations, and the market is inherently unpredictable.
Account for outliers and data gaps in the provided data.
Case in point:

Analyze the provided OHLCV data {self.yesterdayData()} for {self.ticker} and become the ultimate trend detective! Unveil the current market trend, explain your reasoning, and assess the chances of a future shift.
        """
        
    
    def yesterdayData(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.ticker}&apikey={ApiKey}'
        r = requests.get(url)
        rawData = r.json()
        return rawData
    
    def MVdata(self): 
        pass
    
