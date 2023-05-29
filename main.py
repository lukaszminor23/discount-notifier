from requests import get
from bs4 import BeautifulSoup

response = get('https://8a.pl/buty-do-rakow-polautomatycznych-scarpa-ribelle-lite-hd-tonic-tonic')
soup = BeautifulSoup(response.text, 'html.parser')
product = soup.find_all(class_='price-wrapper')

price = ''
for row in product:
    if row['data-price-type'] == 'finalPrice':
        price = row['data-price-amount']
