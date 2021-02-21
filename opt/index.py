import requests
from bs4 import BeautifulSoup as bs4
import re

load_url = "http://www.53cal.jp/areacalendar/?city=1380101&area=1380101435&yy=2021&mm=2"
html = requests.get(load_url)
soup = bs4(html.content, "html.parser")

# ゴミ出しの対象となっている日のリスト
theDays = soup(class_="theday")

for theDay in theDays:
    imgTagSrc = theDay.find('img').get('src')
    day = re.search(r'[0-9]+', imgTagSrc).group()


    title = theDay.find('a').get('title')
    print(day + title)
