import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Pennsylvania_State_University"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', class_="infobox vcard")
# print(table.prettify())

data = []

tag_exclude = 'sup'

for tr in table.find_all('tr', class_=None):
	thisdata = []
	if not (th:=tr.find("th")) or not (thtext:=th.get_text()) or not (tds:=tr.find_all('td')):
		continue
	thisdata.append(thtext)

	for info in tds:
		if info(tag_exclude):
			for info_tag in info.find_all(tag_exclude):
				info_tag.decompose()
		thisdata.append(info.get_text())

	data.append(thisdata)

with open('psu.csv', 'w', newline='', encoding='UTF-8-sig') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["University","The Pennsylvania State University"])
	for i in data:
		writer.writerow(i)
