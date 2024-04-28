from bs4 import BeautifulSoup as BS
import requests

class Web:
    def url_setter(self):
        user = input("Enter a search query: ")
        for i in user:
            if i == " ":
                user = user.replace(" ", "+")
                break
        url = f"https://www.google.com/search?q={user}"
        
        r = requests.get(url)
        soup = BS(r.text, "html.parser")
    
        return soup
    
    def main(self):
        soup = self.url_setter()
        soup = soup.find_all("a")
    
        i = 0
        self.links = []
        for link in soup:
            link = soup[i].get("href")
            #links.append(link)
            i+=1
    
        urls = []
        for link in self.links:
            if link.startswith("/url"):
                urls.append(link)
        return urls
    
if __name__ == "__main__":
    web = Web()
    urls = web.main()
    print(urls)
    print(web.links)

