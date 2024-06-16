from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def setup_driver(chromedriver_path):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome for non-GUI mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver_service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    return driver

def fetch_webpage(url, driver):
    try:
        driver.get(url)
        time.sleep(5)  # Allow some time for the page to load
        html = driver.page_source
        return html
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

    """
    The function `extract_content` takes HTML content as input, removes script and style elements, and
    returns the extracted text content with proper formatting.
    
    :param html: The `extract_content` function you provided is used to extract text content from HTML
    by removing script and style elements. It uses the BeautifulSoup library to parse the HTML and
    extract the text
    :return: The `extract_content` function takes an HTML input, removes script and style elements,
    extracts text content from the HTML, breaks it into lines, removes leading/trailing spaces, breaks
    multi-headlines into a line each, and drops blank lines. Finally, it returns the cleaned text
    content extracted from the HTML.
    """
def extract_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract text from the page, removing script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Get text
    text = soup.get_text(separator="\n")

    # Break into lines and remove leading/trailing spaces on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def save_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    url = input("Enter the URL of the web page: ")
    chromedriver_path = "C:\\Users\\USER\\VOID\\chromedriver-win64\\chromedriver.exe"
    driver = setup_driver(chromedriver_path)
    html = fetch_webpage(url, driver)
    driver.quit()
    if html:
        content = extract_content(html)
        save_to_file(content, "webpage_content.txt")
        print("Content extracted and saved to webpage_content.txt")
