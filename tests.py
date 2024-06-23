# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup

# with sync_playwright() as pw:
#     browser = pw.chromium.launch(headless=False)
#     context = browser.new_context(viewport={"width": 920, "height": 500})
#     page = context.new_page()

#     page.goto("https://finance.yahoo.com", timeout=0)  # go to url

#     content = page.content()
#     soup = BeautifulSoup(content, 'html.parser')
#     page.close()

# header_element = str(soup.find_all(class_="module-hero hero-3-col svelte-6i0owd"))
# header_element = BeautifulSoup(header_element, 'html.parser')

# a_tags = header_element.find_all('a')
# scrape = []

# for tag in a_tags:
#     title = tag.get('title')
#     href = tag.get('href')
    
#     scrape.append({title: href})
#     print({title: href})
    


# # Remove duplicates
# unique_data = []
# seen_items = set()
# for item in scrape:
#     for key, value in item.items():
#         if (key, value) not in seen_items:
#             seen_items.add((key, value))
#             unique_data.append(item)

# # Separate stock quotes and news articles
# stock_quotes = {key: value for item in unique_data for key, value in item.items() if value.startswith('/quote/')}
# news_articles = {key: value for item in unique_data for key, value in item.items() if value.startswith('https://')}

# with open("webpage_content.txt", 'w') as file:
#     file.write(f'{news_articles}\n---\n')



# def link_scraper(link):
#     with sync_playwright() as Play:
#         browser = pw.chromium.launch(headless=True)
#         context = browser.new_context(viewport={"width": 1920, "height": 1080})
#         page = context.new_page()
        
#         page.goto(link)
        
#         html = page.content()
        
#         soup = BeautifulSoup(html, 'html.parser')
        
#         header_element =str( soup.find_all(class_='cass-body'))
        
#         text = BeautifulSoup(header_elemrnts, 'html.parser')
#         text = text.find_all('p')
#         content = []
#         for word in text:
#             content = word.get_text()
#             content.append(content)
            
#         news_report = " ".join(content)
        
#         return news_report

# # import webbrowser

# #     """
# #     The function `open_news` takes a dictionary of news titles and links, filters out the relevant links
# #     based on a keyword, and opens the sorted relevant links in a web browser.
    
# #     :param links_dict: A dictionary containing news titles as keys and corresponding links as values.
# #     For example:
# #     :param keyword: The `open_news` function takes in two parameters: `links_dict`, which is a
# #     dictionary containing titles as keys and links as values, and `keyword`, which is the keyword to
# #     search for in the titles of the news links
# #     :return: If there are relevant news links found for the given keyword, the function will return None
# #     after opening the links in a web browser. If no relevant news links are found, the function will
# #     print a message indicating that and then return None.
# #     """
# # def open_news(links_dict, keyword):
# #     relevant_links = {title: link for title, link in links_dict.items() if keyword.lower() in title.lower()}
    
# #     if not relevant_links:
# #         print("No relevant news found for the given keyword.")
# #         return
    
# #     sorted_links = sorted(relevant_links.items(), key=lambda x: x[0])
# #     for title, link in sorted_links:
# #         print(f"Opening: {title}")
# #         webbrowser.open(link)

# # # Example usage:
# # news_links = {
# #     'Europe stocks rise ahead of Central Bank decisions': 'https://finance.yahoo.com/news/asian-equities-slip-traders-search-224147804.html',
# #     'Both sides in DC draw red lines for 2025 tax fight': 'https://finance.yahoo.com/news/both-sides-in-dc-are-already-drawing-red-lines-over-a-2025-tax-fight-100031317.html',
# #     'Regional banks want to slim down. Hedge funds smell a bargain.': 'https://finance.yahoo.com/news/regional-banks-want-slim-down-093000450.html',
# #     # Add more news links here...
# # }

# # open_news(news_links, "bank")

# # The code snippet you provided is performing the following actions:

# # This code snippet is opening a file named 'previous_five.txt' in append mode ('a+'). It reads the
# # lines from the file into a list called `previous`. It then appends the string "man" to the
# # `previous` list and removes the first element from the list.

# # from chunks import chunk


# # with open('previous_five.txt', 'r', encoding='utf-8') as file:
# #     text = file.read().split('\n---\n')
    
# # text = chunk(text[0])

# # print(text[1]+'\n'+text[2])


from langchain import LangChain

# Define tools
tools = {
    'YouTubeTranscriptFetcher': YouTubeTranscriptFetcher(),
    'NewsFetcher': NewsFetcher(),
    # Add more tools as needed
}

# Define intents and their corresponding tools
intents = {
    'fetch_transcript': 'YouTubeTranscriptFetcher',
    'fetch_news': 'NewsFetcher',
    # Add more intents and corresponding tools
}

# Initialize LangChain
chain = LangChain(tools, intents)

# Process user input
user_input = "I need the latest news about Tesla."
tool, entities = chain.process_input(user_input)

# Activate tool
if tool:
    result = tools[tool].execute(entities)
    print(f"Result: {result}")
else:
    print("Command not recognized. Please try again.")
