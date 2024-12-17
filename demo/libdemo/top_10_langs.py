import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.tiobe.com/tiobe-index/")
contents = resp.text

bs = BeautifulSoup(contents, 'html.parser')

table = bs.find(id = "top20")
rows = table.find_all("tr")
for row in rows[1:11]:
    cols = row.find_all("td")
    lang = cols[4].text
    rating = cols[5].text
    print(f"{lang:30} {rating:6}")
