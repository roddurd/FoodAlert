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

menus = html_soup.findAll('div',{'class':'col-sm-6 col-md-4'})

being_served = (False,None)
dining_hall = None

for menu in menus:
    dining_hall = str(menu.h3.text)
    menu = str(menu).lower()
    if fav_food in menu:
        being_served = (True,dining_hall)

result = "Yay! That food is being served at " + being_served[1] + " today!" if being_served[0] else "Sorry, that food is not being served today."

print(result)


        
