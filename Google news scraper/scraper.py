import requests  # importing request library to make https request to google news

# importing beautiful soup to extract data from the website
from bs4 import BeautifulSoup

import csv

requirement = int(input(
    "Please Enter the number of articles that is required in the excel file.\n"))

stub = "https://www.news.google.com"
URL = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html5lib')
extracted_items = []


for row in soup.findAll('a', attrs={'class': 'DY5T1d RZIKme'})[:requirement]:

    extracted_item = {}
    extracted_item['Headline'] = row.text
    extracted_item['Link of news article'] = rf"{stub + row['href'][1:]}"

    extracted_items.append(extracted_item)


filename = "news.csv"
with open(filename, 'w', newline="", encoding='utf8') as f:
    w = csv.DictWriter(f, ['Headline', 'Link of news article'])
    w.writeheader()
    for extracted_item in extracted_items:
        w.writerow(extracted_item)
