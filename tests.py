


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





# from typing import Any, List
# from tools import youtube, search

# import re

# # Step 1: Define multiple functions
# def call(name: str):
#     print(f"Calling {name}...")

# def text(message: str):
#     print(f"Texting: {message}")

# def shoot(target: str):
#     print(f"Shooting at {target}")

# # Step 2: Create a mapping of function names to functions
# function_map = {
#     "call": call,
#     "text": text,
#     "shoot": shoot
# }

# # Step 3: Create a random string with potential function calls
# random_string = "I will use the call func to try and call Alice call('Alice'))"

# # Step 4: Use regular expressions to find and extract function calls
# pattern = r"(call|text|shoot)\([\'\"](.*?)[\'\"]\)"
# matches = re.findall(pattern, random_string)

# # Step 5: Execute each extracted function call using the mapping
# print(matches)


# foo = ['a', 'b', 'c', 'd']

# goo = ['goon', 'foon']

# hee = ['haaa', 'heee', 'hooo']
# for z in hee:
#     for x in goo:
#         for y in foo:
#             if y == 'd' or 'heee' or 'goon':
                
#             print([z, x, y])
from youtube_transcript_api import YouTubeTranscriptApi as yta
from youtubesearchpython import VideosSearch

def run(text: str):
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
tex = 'a'

for i in tex:
    exec("vid = run('tesla stock price today')", globals())

print(vid)
