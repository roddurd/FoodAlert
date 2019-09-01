from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

url = 'https://hospitality.usc.edu/residential-dining-menus/'

client = urlopen(url)
html = client.read()
client.close()

html_soup = soup(html, "html.parser")

menus = html_soup.findAll('ul',{'class':'menu-item-list'})

for menu in menus:
    items = menu.li.text
    print('item: \n', items, '\n\n')
