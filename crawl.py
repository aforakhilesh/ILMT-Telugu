from bs4 import BeautifulSoup
import requests
import json
import time
import re
import pandas as pd
from queue import Queue

global q
maxQueue = 2000
q = Queue(maxsize = maxQueue)

global queue,tq
queue = []
tq = []

# This function crawls till specified depth and breadth and then stops after returning the inter-wiki links.
def extract_interwikilinks(url):
    if(q.qsize()>maxQueue):
        return
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup = soup.find("div", {"id":"mw-content-text"})

    links = soup.find_all("a", href = True)

    remlist = ["మూలాల","v","t"]

    for link in links:
        if link.text not in tq and link['href'][:7] == "/wiki/%" and link.text not in remlist and len(link.text)>0:
            queue.append(link['href'])
            tq.append(link.text)
            q.put(str("https://te.wikipedia.org/"+link['href']))
    


def main():
    global q
    # Update the next line based on the source url we want to crawl from.
    url = "https://te.wikipedia.org/wiki/%E0%B0%AD%E0%B0%BE%E0%B0%B0%E0%B0%A4_%E0%B0%B0%E0%B0%BE%E0%B0%9C%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%82%E0%B0%97%E0%B0%82"
    q.put(url)
    while(not q.empty()):

        extract_interwikilinks(q.get())
        
        if(q.qsize()>int(maxQueue*0.9)):
            return
    
        data = list(zip(tq,queue))
        df = pd.DataFrame(data,columns=['titles','Urls'])
        df.to_csv('links.csv')

if __name__ == "__main__":
    main()



