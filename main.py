import requests
from bs4 import BeautifulSoup

response=requests.get('https://www.ceneo.pl/32622086#tab=reviews')
pageDOM=BeautifulSoup(response.text, 'html.parser')
opinion=pageDOM.select("div.js_product-review").pop(0)
opinionId=opinion["data-entry-id"]
author= opinion.select("span.user-post__author-name").pop(0).get_text().strip()
try:
    rcmd=opinion.select("span.user-post__author-recomendation > em").pop(0).get_text().strip()
except IndexError:
    rcmd=None
stars=opinion.select("span.user-post__score-count").pop(0).get_text().strip()
content=opinion.select("div.user-post__text").pop(0).get_text().strip()
pros=opinion.select("div[class*=\"positives\"] ~ div.review-feature__item")
pros=[item.get_text().strip() for item in pros]
cons=opinion.select("div[class*=\"negatives\"] ~ div.review-feature__item")
cons=[item.get_text().strip() for item in cons]
try:
    purchased=opinion.select("div.review-pz").pop(0).get_text().strip()
except IndexError:
    purchased=None
publishDate=opinion.select("span.user-post__published > time:nth-child(1)").pop(0)["datetime"].strip()
try:
    purchaseDate=opinion.select("span.user-post__published > time:nth-child(2)").pop(0)["datetime"].strip()
except IndexError:
    purchaseDate=None
useful=opinion.select("span[id^=\"votes-yes\"]").pop(0).get_text().strip()
useless=opinion.select("span[id^=\"votes-no\"]").pop(0).get_text().strip()

print(author, rcmd, stars, content, pros, cons, purchased, publishDate, purchaseDate, useful, useless, sep="\n")