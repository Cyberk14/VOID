# this file will be used to see/spot the info the internet an the files the use r will have complied inform of .pdf files and images.

from pypdf import PdfReader
from playwright.sync_api import sync_playwright

class _eyes:
    def read_pdf(self, data):
        paper = PdfReader("paper.pdf")
        content = paper.pages[0]
        
    def read_web(self, *args):
        web = _web()
        google_search = web.google(args)
        
        market_news = web.market_news()
        
        return google_search, market_news
    
    
class _web:
    def google(self, query):
        def browser():
            browser = P.Chromium.launch()
            page = browser.new_page()
            page.goto(f"https://google.com/?q={query}")
            page.screenshot("Control/Brain/web_pic.png")
    
            page.close()
        with sync_playwright as P:
            browser()
            
    def market_news():
        def browser():
            browser = P.Chromium.launch()
            page = browser.new_page()
            page.goto("https://www.marketwatch.com/")
            page.screenshot("Control/Brain/web_pic.png")
    
            page.close()
        with sync_playwright as P:
            browser()
            
