from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

fav_food = input("What food are you looking for? Use the exact name (case insensitive):")

while not fav_food:
    fav_food = input("What food are you looking for? Use the exact name (case insensitive):") 
fav_food = fav_food.lower()

url = 'https://hospitality.usc.edu/residential-dining-menus/'

client = urlopen(url)
html = client.read()
client.close()

html_soup = soup(html, "html.parser")

menus = html_soup.findAll('ul',{'class':'menu-item-list'})

being_served = False

for menu in menus:
    menu = str(menu).lower()
    if fav_food in menu:
        being_served = True

result = "Yay! That food is being served today!" if being_served else "Sorry, that food is not being served today."

print(result)


        
