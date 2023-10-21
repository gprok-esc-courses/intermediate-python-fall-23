import requests
from xml.etree.ElementTree import fromstring

rss_feed = requests.get('https://www.yahoo.com/news/rss/world')
content = rss_feed.content

root_node = fromstring(content)

for item in root_node.iter('item'):
    title = item.find('title')
    print(title.text)
