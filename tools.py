from youtube_transcript_api import YouTubeTranscriptApi as yta
from youtubesearchpython import VideosSearch
from playwright.sync_api import sync_playwright
from typing import Any




# def tool(func: Any):
#     def wrapper(*args: Any):
#         func_name, desc, how_to = func()
#         tool_list[func_name] = {'description': desc,
#                                 'how to run': how_to}
        
#     return wrapper

class youtube:
    def register(*args):
        name = 'Youtube'
        desc = '''
        This is used to retrieve data from youtube
        '''
        how_to = 'Youtube.run(text: str)'
        
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
    
class Web:
    def register(*args):
        name = 'web crawler'
        desc = """
        A tool used to browse the web as a real human would.
        """
        how_to = 'Web.run(query: str)'
        
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
