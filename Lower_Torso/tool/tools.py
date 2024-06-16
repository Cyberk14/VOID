from playwright.sync_api import sync_playwright

tool_list = {
    
}

def tool(func):
    def wrapper():
        func_name, desc, _func_run = func
        tool_list['Tool Name'] = {'func_name': func_name,
                                  'desc': desc,
                                  'how to run': _func_run}
    return wrapper

class _web:
    @tool
    def google(self, query):
        def browser():
            browser = P.Chromium.launch()
            page = browser.new_page()
            page.goto(f"https://google.com/?q={query}")
            page.screenshot("Control/Brain/web_pic.png")
    
            page.close()
        with sync_playwright as P: # type: ignore
            browser()

    @tool
    def market_news(self):
        def browser():
            browser = P.Chromium.launch()
            page = browser.new_page()
            page.goto("https://www.marketwatch.com/")
            page.screenshot("Control/Brain/web_pic.png")
    
            page.close()
        with sync_playwright as P: # type: ignore
            browser()
            