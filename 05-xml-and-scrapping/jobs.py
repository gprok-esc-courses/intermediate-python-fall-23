import requests
from bs4 import BeautifulSoup

job_page = requests.get('https://www.profesia.sk/en/work/?search_anywhere=python')

soup = BeautifulSoup(job_page.content, 'html.parser')

job_titles = soup.find_all('span', class_='title')

for title in job_titles:
    print(title.text)

