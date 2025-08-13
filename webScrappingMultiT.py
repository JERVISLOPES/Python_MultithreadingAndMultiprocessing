import threading 
import requests
from bs4 import BeautifulSoup

urls=['https://beautiful-soup-4.readthedocs.io/en/latest/',
      'https://beautiful-soup-4.readthedocs.io/en/latest/#making-the-soup',
      'https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start']

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
        thread.join()

print("All threads have finished execution.")