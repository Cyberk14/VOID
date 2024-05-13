from bs4 import BeautifulSoup as BS
import requests

class Web:
    def factualData(self):
        user = input("Input your search query: ")
        for i in user:
            if i == " ":
                user = user.replace(" ", "+")
                break
        url = f"https://www.google.com/search?q={user}"
        
        r = requests.get(url)
        soup = BS(r.text, "html.parser")
    
        return soup
    
    def dynamicInfo(self, site= None)
        default = "https:/"
        
        
if __name__ == "__main__":
    web = Web()
    urls = web.main()
    print(urls)
    print(web.links)

