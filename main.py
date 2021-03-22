import requests

response=requests.get('https://www.ceneo.pl/32622086#tab=reviews')
print(response.text)