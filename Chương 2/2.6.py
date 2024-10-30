import requests
import xml.etree.ElementTree as ET
import csv

url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
response = requests.get(url)

with open('rssfeed.xml', 'wb') as file:
    file.write(response.content)

tree = ET.fromstring(response.content)
items = tree.findall('.//item')

with open('news.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Link', 'Description'])

    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        description = item.find('description').text
        writer.writerow([title, link, description])