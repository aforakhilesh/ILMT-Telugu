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
    df = pd.read_csv("medical_links_containing_links.csv")
    for i in range(len(df)):
        print(i)
        try:
            t = extract(df["Link"][i])
        except:
            continue
        # Can also update the output path if needed.
        string  = "./MedicalTask/%s.txt" % i
        WordCount += len(t.split(" "))
        t = sent_tokenize(t)
        SentenceCount += len(t)
        try:
            with open(string, "w") as f:
                f.write(df["Title"][i])
                f.write("\n")
                f.write("\n")
                f.write(df["Link"][i])
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

