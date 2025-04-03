from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

query = "programming"
url = urlunparse(("https", "www.bing.com", "/search", "", urlencode({"q": query}), ""))
custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
req = Request(url, headers={"User-Agent": custom_user_agent})
page = urlopen(req)
# Further code I've left unmodified
soup = BeautifulSoup(page.read(), features='lxml')
links = soup.findAll("a")
for link in links:
    print(link["href"])
