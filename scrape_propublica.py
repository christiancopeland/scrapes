from curl_cffi import requests
from selectolax.parser import HTMLParser
import json
from utils import write_json
from datetime import datetime


r = requests.get(url="https://www.propublica.org", impersonate="chrome101")

html = HTMLParser(r.text)

current_time = datetime.now()

print(f"Propublica Collection for {current_time}")

titles = list()

news_articles = html.css('div.story-card__description')
print(news_articles)
for div in news_articles:
        titles.append({'Title': div.html.title(), "Text": div.text()})
        print('\n##### Center News Div Tags #####\n')
        print(div.text(), div.html.title())
        print('\n##### Center News Div Tags #####\n')
    
news_articles = html.css('div#r7.pp-module.module-popular')
print(news_articles)
for div in news_articles:
    titles.append({"Title": div.html.title(), "Text": div.text()})
    print('\n##### Most Read Section #####\n')
    print(div.text(), div.html.title())
    print('\n##### Most Read Section #####\n')

write_json(json_object=titles, indent=4, filepath= f"/home/bron/AI/local_stuff/book_qa/propublica_collection/{current_time}-propublica.json")

