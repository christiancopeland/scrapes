from curl_cffi import requests
from selectolax.parser import HTMLParser
import json
from utils import write_json
from datetime import datetime



r = requests.get(url="https://www.local3news.com", impersonate="chrome101")

html = HTMLParser(r.text)

current_time = datetime.now()

print(f"Local3News Collection for {current_time}")

titles = list()

news_articles = html.css('a')
for div in news_articles:
    if "card-body" and "tnt-asset-link" in div.html:
        titles.append({"Title": div.html.title(), "Text": div.text()})
        print(div.text(), div.html.title())

write_json(json_object=titles, indent=4, filepath=f"/home/bron/AI/local_stuff/book_qa/local3news_collection/{current_time}-Local3News.json")



