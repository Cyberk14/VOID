import asyncio
from duckduckgo_search import DDGS
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import random

# Set the event loop policy to WindowsProactorEventLoopPolicy for compatibility
if hasattr(asyncio, 'WindowsProactorEventLoopPolicy'):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

class Searcher:
    def human_like_wait(self, min_delay=2, max_delay=5):
        time.sleep(random.uniform(min_delay, max_delay))

    def run(self, text: str):
        try:
            print("searching")
            results = DDGS().text(text, region='wt-wt', safesearch='off', timelimit='y', max_results=1)
            
            if not results:
                print("No results found.")
                return []

            url = results[0]['href']
            print(url)

            self.human_like_wait()

            with sync_playwright() as pw:
                browser = pw.chromium.launch(headless=True)
                context = browser.new_context(
                    viewport={"width": 920, "height": 500},
                    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    locale='en-US',
                    timezone_id='America/New_York'
                )
                page = context.new_page()

                page.goto(url, timeout=0)

                # Simulate human-like interaction
                self.human_like_wait()
                page.mouse.move(100, 200)
                self.human_like_wait()
                page.mouse.move(300, 400)
                self.human_like_wait()

                # Wait for the page to load
                page.wait_for_load_state('networkidle')
                content = page.content()
                page.close()
                context.close()
                browser.close()

            soup = BeautifulSoup(content, 'html.parser')
            p_tags = [p.get_text() for p in soup.find_all('p')]
            
            return p_tags
        except Exception as error:
            print('An error occurred when running Search: ', error)

# Example usage
searcher = Searcher()
text_to_search = "gold market sentiment articles"
p_tags = searcher.run(text_to_search)
print(p_tags)



# import matplotlib.pyplot as plt
# import networkx as nx

# # Initialize a directed graph
# G = nx.DiGraph()

# # Add entities (nodes) to the graph
# entities = [
#     ("Retail traders", "Group"),
#     ("Market", "General Term"),
#     ("Gold", "Commodity"),
#     ("US Crude Oil", "Commodity"),
#     ("S&P 500", "Index"),
#     ("DailyFX", "Organization"),
#     ("Nick Cawley", "Person"),
#     ("Twitter", "Platform"),
#     ("Yesterday", "Date"),
#     ("Past week", "Date")
# ]

# # Add the nodes with entity type as an attribute
# for entity, entity_type in entities:
#     G.add_node(entity, type=entity_type)

# # Add relationships (edges) to the graph
# relationships = [
#     ("Retail traders", "are in", "long positions"),
#     ("Retail traders", "are in", "short positions"),
#     ("Short positions", "ratio of", "1.01 to 1, short-to-long"),
#     ("Long positions", "decreased by", "13.24% since yesterday"),
#     ("Long positions", "decreased by", "13.73% over the past week"),
#     ("Short positions", "increased by", "8.36% daily"),
#     ("Short positions", "increased by", "6.44% weekly"),
#     ("Net-short positioning", "implies potential for", "Gold price appreciation"),
#     ("Short bias", "strengthens", "contrarian bullish view on Gold"),
#     ("Retail traders", "are net-long", "US Crude Oil"),
#     ("Long positions", "outweigh", "short positions, 1.40 to 1"),
#     ("Net-long traders", "decreased by", "0.43% daily"),
#     ("Net-long traders", "increased by", "7.19% weekly"),
#     ("Net-short traders", "grown by", "4.31% since yesterday"),
#     ("Net-short traders", "declined by", "14.98% over the week"),
#     ("Net-long majority", "implies potential for", "US Crude price decreases"),
#     ("Short-term and medium-term changes", "yield ambiguous outlook for", "Oil - US Crude"),
#     ("Retail trader data", "reveals", "bearish tilt, S&P 500"),
#     ("Net-long traders", "grown by", "13.58% since yesterday"),
#     ("Net-long traders", "grown by", "6.75% over the week"),
#     ("Net-short traders", "declined by", "8.07% daily"),
#     ("Net-short traders", "declined by", "2.91% weekly"),
#     ("Dominant net-short sentiment", "suggests continued", "US 500 price appreciation"),
#     ("Decline in net-short positions", "indicates possible reversal in", "current US 500 uptrend"),
#     ("DailyFX", "provides", "forex news and technical analysis"),
#     ("Nick Cawley", "contact via", "Twitter @nickcawley1")
# ]

# # Add the edges with relationship type as an attribute
# for source, relationship, target in relationships:
#     G.add_edge(source, target, type=relationship)

# # Draw the graph
# pos = nx.spring_layout(G, seed=42)  # positions for all nodes
# plt.figure(figsize=(15, 10))
# nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=10, font_weight="bold", arrows=True, arrowstyle='->', arrowsize=20)
# edge_labels = nx.get_edge_attributes(G, 'type')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.5)
# plt.title("Entity-Relationship Graph")
# plt.show()

# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup

# def run():
#     # results = DDGS().text('live free or die filetype:pdf', region='wt-wt', safesearch='off', timelimit='y', max_results=1)
    
    
#     with sync_playwright() as pw:
#         browser = pw.chromium.launch(headless=False)
#         context = browser.new_context(viewport={"width": 920, "height": 500})
#         page = context.new_page()

#         page.goto("https://finance.yahoo.com", timeout=0)  # go to url

#         content = page.content()
#         soup = BeautifulSoup(content, 'html.parser').get_text()
#         page.close()
#         print(soup)
#     return soup



# run()
import time


