from bs4 import BeautifulSoup
import requests
import json
import time
import re
import pandas as pd

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize


def extract(url):
    text = ""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    main = soup.find_all("p")[0].find_next_siblings()
    text = text + soup.find_all("p")[0].text

    for item in main:
        if item.name == "p" or item.name == "ol" or item.name == "ul":
            text = text + item.text
    t = re.sub("[/[0-9/]*]", "",text)
    return t


global SentenceCount
SentenceCount = 0
global WordCount
WordCount = 0

def main():
   
    global SentenceCount
    global WordCount

    # Update the next line based on the file that contains the links to articles.
    df = pd.read_csv("links.csv")

    # Change the number of files by changing the value in range(), keeping len(df) runs for all links, range(n) runs for "n" links.
    for i in range(len(df)):
        
        # change "te" to other language tags if needed, (like "hi","ur","bn")..
        try:
            t = extract("https://te.wikipedia.org"+str(df["Urls"][i]))
        except:
            continue

        # Can also update the output path if needed.
        string  = "./%s.txt" % i
        WordCount += len(t.split(" "))
        t = sent_tokenize(t)
        SentenceCount += len(t)

        try:
            with open(string, "w") as f:
                f.write(df["titles"][i])
                f.write("\n")
                f.write("\n")
                f.write(df["Urls"][i])
                f.write("\n")
                f.write("\n")
                for line in t:
                    f.write(line)
                    f.write("\n")
                f.close()
        except:
            pass


if __name__ == '__main__':
    main()
    print("Total Sentences: ", SentenceCount)
    print("\n")
    print("Total Words: ", WordCount)

