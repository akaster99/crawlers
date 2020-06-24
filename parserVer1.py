import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


req = requests.get('https://www.fmkorea.com/?vid=&mid=best&category=&listStyle=webzine&search_keyword=%EB%A6%AC%EB%B2%84%ED%92%80&search_target=title_content')

html = req.text

soup = BeautifulSoup(html, 'html.parser')


my_titles = soup.select(
    'ul > li > div > h3 > a'
    )

data = {}

for title in my_titles:
    data[title.text] = title.get('href')
    
with open(os.path.join(BASE_DIR, 'result.json'), 'w+', encoding='utf-8') as json_file:
    json.dump(data, json_file,ensure_ascii=False)
