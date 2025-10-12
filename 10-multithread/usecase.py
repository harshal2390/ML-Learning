import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/tutorials/llm_chain/',
    'https://python.langchain.com/docs/tutorials/chatbot/'
]

def fetch_content(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        # print only first 300 chars safely
        print(f"Fetched {len(text)} characters from {url}\n")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All pages fetched ")
