import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.srikanthtechnologies.com")
contents = resp.text

bs = BeautifulSoup(contents, 'html.parser')

table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
if table is None:
    print('Sorry! Could not get details')
    exit(1)


rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    course = cols[1].text
    timings = cols[2].text
    stdate = cols[3].text
    print(f"{course:50} {stdate:10}  {timings:15}")
