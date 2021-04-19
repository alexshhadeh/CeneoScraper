import requests
from bs4 import BeautifulSoup
import json

def extractComponent(opinion, selector, attribute=None):
    try:
        if attribute:
            return opinion.select(selector).pop(0)[attribute].strip()
        if attribute is None:
            return opinion.select(selector).pop(0).get_text().strip()
        return [item.get_text().strip() for item in opinion.select(selector)]
    except IndexError:
        return None

#productId="32622086"
#productId="97065427"
productId=input("Podaj kod produktu: ")
response=requests.get(f'https://www.ceneo.pl/{productId}#tab=reviews')
page=2
opinionsList=[]

while response:
    pageDOM=BeautifulSoup(response.text, 'html.parser')
    opinions=pageDOM.select("div.js_product-review")

    #print(page)

    for opinion in opinions:
        opinionId=opinion["data-entry-id"]
        author=extractComponent(opinion, "span.user-post__author-name")
        rcmd=extractComponent(opinion, "span.user-post__author-recomendation > em")
        stars=extractComponent(opinion, "span.user-post__score-count")
        content=extractComponent(opinion, "div.user-post__text")
        ##########
        pros=extractComponent(opinion, "div[class*=\"positives\"] ~ div.review-feature__item", False)
        cons=extractComponent(opinion, "div[class*=\"negatives\"] ~ div.review-feature__item", False)
        ##########
        purchased=extractComponent(opinion, "div.review-pz")
        ##########
        publishDate=extractComponent(opinion, "span.user-post__published > time:nth-child(1)", "datetime")
        purchaseDate=extractComponent(opinion, "span.user-post__published > time:nth-child(2)", "datetime")
        ##########
        useful=extractComponent(opinion, "span[id^=\"votes-yes\"]")
        useless=extractComponent(opinion, "span[id^=\"votes-no\"]")

        rcmd=True if rcmd=="Polecam" else False
        stars=float(stars.split("/")[0].replace(",", "."))
        content=content.replace("\n", " ").replace("\r", " ")
        purchased=bool(purchased)
        useful=int(useful)
        useless=int(useless)

        opinionDict={
            "opinionId": opinionId,
            "author": author,
            "rcmd": rcmd,
            "stars": stars,
            "content": content,
            "pros": pros,
            "cons": cons,
            "purchased": purchased,
            "publishDate": publishDate,
            "purchaseDate": purchaseDate,
            "useful": useful,
            "useless": useless
        }

        opinionsList.append(opinionDict)

    response=requests.get(f'https://www.ceneo.pl/{productId}/opinie-{str(page)}', allow_redirects=False)
    if response.status_code==200:
        page+=1
    else:
        break

with open(f"./opinions/{productId}.json", "w", encoding="UTF-8") as f:
    json.dump(opinionsList, f, indent=4, ensure_ascii=False)

#print(json.dumps(opinionsList, indent=4, ensure_ascii=False))