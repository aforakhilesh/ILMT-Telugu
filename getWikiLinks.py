import pandas as pd
import wikipedia
import selenium
from selenium import webdriver

driver = webdriver.Firefox()

url_list = [
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%AE%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AA%E0%B0%B6%E0%B1%81_%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%82",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AD%E0%B0%BE%E0%B0%B0%E0%B0%A4_%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF_%E0%B0%AE%E0%B0%82%E0%B0%A1%E0%B0%B2%E0%B0%BF",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AD%E0%B0%BE%E0%B0%B0%E0%B0%A4%E0%B0%A6%E0%B1%87%E0%B0%B6%E0%B0%82%E0%B0%B2%E0%B1%8B_%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF_%E0%B0%B5%E0%B0%BF%E0%B0%A6%E0%B1%8D%E0%B0%AF",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%94%E0%B0%B7%E0%B0%A7%E0%B0%BE%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%9F%E0%B1%80%E0%B0%95%E0%B0%BE%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AE%E0%B0%82%E0%B0%A6%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B0%E0%B1%8B%E0%B0%97_%E0%B0%B2%E0%B0%95%E0%B1%8D%E0%B0%B7%E0%B0%A3%E0%B0%BE%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF_%E0%B0%85%E0%B0%A4%E0%B1%8D%E0%B0%AF%E0%B0%B5%E0%B0%B8%E0%B0%B0%E0%B0%BE%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF_%E0%B0%B5%E0%B0%BF%E0%B0%A6%E0%B1%8D%E0%B0%AF",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%87%E0%B0%82%E0%B0%AA%E0%B1%8D%E0%B0%B2%E0%B0%BE%E0%B0%82%E0%B0%9F%E0%B1%8D",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF_%E0%B0%AA%E0%B0%B0%E0%B0%BF%E0%B0%95%E0%B0%B0%E0%B0%BE%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF_%E0%B0%AA%E0%B0%B0%E0%B1%80%E0%B0%95%E0%B1%8D%E0%B0%B7%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B0%E0%B0%95%E0%B1%8D%E0%B0%A4_%E0%B0%AA%E0%B0%B0%E0%B1%80%E0%B0%95%E0%B1%8D%E0%B0%B7%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B0%BF_%E0%B0%B2%E0%B0%95%E0%B1%8D%E0%B0%B7%E0%B0%A3%E0%B0%BE%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%A8%E0%B1%8A%E0%B0%AA%E0%B1%8D%E0%B0%AA%E0%B0%BF",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B0%BF%E0%B0%95%E0%B0%B2%E0%B0%BE%E0%B0%82%E0%B0%97%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%85%E0%B0%82%E0%B0%97%E0%B0%B5%E0%B1%88%E0%B0%95%E0%B0%B2%E0%B1%8D%E0%B0%AF%E0%B0%82",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%88%E0%B0%B0%E0%B0%B2%E0%B1%8D_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%8E%E0%B0%AF%E0%B0%BF%E0%B0%A1%E0%B1%8D%E0%B0%B8%E0%B1%8D",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%85%E0%B0%82%E0%B0%9F%E0%B1%81_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%8E%E0%B0%AE%E0%B1%81%E0%B0%95%E0%B0%B2_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%95%E0%B0%82%E0%B0%9F%E0%B0%BF_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%95%E0%B0%82%E0%B0%A1%E0%B0%B0%E0%B0%BE%E0%B0%B2_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%95%E0%B1%80%E0%B0%B3%E0%B1%8D%E0%B0%B3_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%9A%E0%B0%B0%E0%B1%8D%E0%B0%AE_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%9A%E0%B0%BF%E0%B0%A8%E0%B1%8D%E0%B0%A8%E0%B0%AA%E0%B0%BF%E0%B0%B2%E0%B1%8D%E0%B0%B2%E0%B0%B2_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%9C%E0%B0%A8%E0%B1%8D%E0%B0%AF%E0%B1%81_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%9C%E0%B1%80%E0%B0%B0%E0%B1%8D%E0%B0%A3%E0%B0%95%E0%B1%8B%E0%B0%B6_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AE%E0%B0%BE%E0%B0%A8%E0%B0%B8%E0%B0%BF%E0%B0%95_%E0%B0%B0%E0%B1%81%E0%B0%97%E0%B1%8D%E0%B0%AE%E0%B0%A4%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B6%E0%B0%BE%E0%B0%B0%E0%B1%80%E0%B0%B0%E0%B0%95_%E0%B0%B8%E0%B0%AE%E0%B0%B8%E0%B1%8D%E0%B0%AF%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B6%E0%B1%8D%E0%B0%B5%E0%B0%BE%E0%B0%B8%E0%B0%95%E0%B1%8B%E0%B0%B6_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B8%E0%B0%BF%E0%B0%82%E0%B0%A1%E0%B1%8D%E0%B0%B0%E0%B1%8B%E0%B0%AE%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AE%E0%B0%BE%E0%B0%A8%E0%B0%B8%E0%B0%BF%E0%B0%95_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AE%E0%B0%BE%E0%B0%A8%E0%B0%B8%E0%B0%BF%E0%B0%95_%E0%B0%B0%E0%B1%81%E0%B0%97%E0%B1%8D%E0%B0%AE%E0%B0%A4%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B0%E0%B0%95%E0%B1%8D%E0%B0%A4_%E0%B0%B8%E0%B0%82%E0%B0%AC%E0%B0%82%E0%B0%A7_%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A7%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B2%E0%B0%BF%E0%B0%82%E0%B0%AA%E0%B1%8B%E0%B0%AE%E0%B0%BE",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B2%E0%B1%81%E0%B0%95%E0%B1%87%E0%B0%AE%E0%B0%BF%E0%B0%AF%E0%B0%BE",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%86%E0%B0%B0%E0%B1%8B%E0%B0%97%E0%B1%8D%E0%B0%AF_%E0%B0%9A%E0%B0%BF%E0%B0%9F%E0%B1%8D%E0%B0%95%E0%B0%BE%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%86%E0%B0%B0%E0%B1%8B%E0%B0%97%E0%B1%8D%E0%B0%AF_%E0%B0%B8%E0%B0%AE%E0%B0%B8%E0%B1%8D%E0%B0%AF%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%86%E0%B0%B8%E0%B1%81%E0%B0%AA%E0%B0%A4%E0%B1%8D%E0%B0%B0%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%A8%E0%B0%B0%E0%B1%8D%E0%B0%B8%E0%B0%BF%E0%B0%82%E0%B0%97%E0%B1%8D",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AA%E0%B1%8D%E0%B0%B0%E0%B0%9C%E0%B0%BE%E0%B0%B0%E0%B1%8B%E0%B0%97%E0%B1%8D%E0%B0%AF%E0%B0%82",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AE%E0%B0%B9%E0%B0%BF%E0%B0%B3%E0%B0%BE_%E0%B0%86%E0%B0%B0%E0%B1%8B%E0%B0%97%E0%B1%8D%E0%B0%AF%E0%B0%82",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AF%E0%B1%8B%E0%B0%97%E0%B0%BE",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%AE%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%AF%E0%B0%BE%E0%B0%AE%E0%B0%82",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%8D%E0%B0%AF%E0%B0%B8%E0%B0%A8%E0%B0%BE%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AE%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%82",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%95%E0%B1%8D%E0%B0%AF%E0%B0%BE%E0%B0%A8%E0%B1%8D%E0%B0%B8%E0%B0%B0%E0%B1%8D_%E0%B0%86%E0%B0%B8%E0%B1%81%E0%B0%AA%E0%B0%A4%E0%B1%8D%E0%B0%B0%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%A4%E0%B1%86%E0%B0%B2%E0%B0%82%E0%B0%97%E0%B0%BE%E0%B0%A3_%E0%B0%86%E0%B0%B8%E0%B1%81%E0%B0%AA%E0%B0%A4%E0%B1%8D%E0%B0%B0%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%97%E0%B1%88%E0%B0%A8%E0%B0%95%E0%B0%BE%E0%B0%B2%E0%B0%9C%E0%B1%80",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%8B%E0%B0%A4%E0%B1%81_%E0%B0%9A%E0%B0%95%E0%B1%8D%E0%B0%B0%E0%B0%82",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AE%E0%B1%86%E0%B0%A8%E0%B1%8B%E0%B0%AA%E0%B0%BE%E0%B0%9C%E0%B1%8D",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%95%E0%B1%8D%E0%B0%B0%E0%B0%BF%E0%B0%AF%E0%B0%BE_%E0%B0%AF%E0%B1%8B%E0%B0%97%E0%B0%AE%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AF%E0%B1%8B%E0%B0%97%E0%B0%BE%E0%B0%9A%E0%B0%BE%E0%B0%B0%E0%B1%8D%E0%B0%AF%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%95%E0%B1%8D%E0%B0%B0%E0%B0%BF%E0%B0%AF%E0%B0%BE%E0%B0%AF%E0%B1%8B%E0%B0%97_%E0%B0%97%E0%B1%81%E0%B0%B0%E0%B1%81%E0%B0%B5%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%AD%E0%B0%BE%E0%B0%B0%E0%B0%A4%E0%B1%80%E0%B0%AF_%E0%B0%AF%E0%B1%8B%E0%B0%97%E0%B0%BE%E0%B0%9A%E0%B0%BE%E0%B0%B0%E0%B1%8D%E0%B0%AF%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%A4%E0%B0%AE%E0%B0%BF%E0%B0%B3%E0%B0%A8%E0%B0%BE%E0%B0%A1%E0%B1%81_%E0%B0%AF%E0%B1%8B%E0%B0%97%E0%B0%BE%E0%B0%9A%E0%B0%BE%E0%B0%B0%E0%B1%8D%E0%B0%AF%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%86%E0%B0%82%E0%B0%A7%E0%B1%8D%E0%B0%B0%E0%B0%AA%E0%B1%8D%E0%B0%B0%E0%B0%A6%E0%B1%87%E0%B0%B6%E0%B1%8D_%E0%B0%AF%E0%B1%8B%E0%B0%97%E0%B0%BE%E0%B0%9A%E0%B0%BE%E0%B0%B0%E0%B1%8D%E0%B0%AF%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%A4%E0%B1%82%E0%B0%B0%E0%B1%8D%E0%B0%AA%E0%B1%81_%E0%B0%97%E0%B1%8B%E0%B0%A6%E0%B0%BE%E0%B0%B5%E0%B0%B0%E0%B0%BF_%E0%B0%9C%E0%B0%BF%E0%B0%B2%E0%B1%8D%E0%B0%B2%E0%B0%BE_%E0%B0%AF%E0%B1%8B%E0%B0%97%E0%B0%BE%E0%B0%9A%E0%B0%BE%E0%B0%B0%E0%B1%8D%E0%B0%AF%E0%B1%81%E0%B0%B2%E0%B1%81",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%86%E0%B0%B0%E0%B1%8B%E0%B0%97%E0%B1%8D%E0%B0%AF%E0%B0%82",
    "https://te.wikipedia.org/wiki/%E0%B0%B5%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B0%82:%E0%B0%B5%E0%B1%88%E0%B0%A6%E0%B1%8D%E0%B0%AF%E0%B0%AE%E0%B1%81"
]



# driver.get(url1)

title = []
link = []

def extract_links(urllinks):
    for url in urllinks:
        driver.get(url)
        try:
            a = driver.find_element_by_xpath("//div[@id='mw-pages']")
            # a = find_element(by=By.XPATH, value="//div[@id='mw-pages']")
            b = a.find_elements_by_class_name("mw-category-group")
            for item in b:
                items = item.find_elements_by_tag_name("a")
                for link_old in items:
                    # base = "https://kn.wikipedia.org/wiki"
                    link.append(link_old.get_attribute("href"))
                    title.append(str(link_old.get_attribute("title")))
        except:
            pass

    data = list(zip(title,link))
    df = pd.DataFrame(data,columns=['Title','Link'])
    df.to_csv('medical_links_containing_links.csv')

if __name__ == '__main__':
    extract_links(url_list)
    print(len(set(link)))

    
