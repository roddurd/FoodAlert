from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

fav_food = input("What food are you looking for? Double check your spelling (case insensitive): ") 

while not fav_food:
    fav_food = input("What food are you looking for? Double check your spelling (case insensitive): ") 
fav_food = fav_food.lower()

url = 'https://hospitality.usc.edu/residential-dining-menus/'

client = urlopen(url)
html = client.read()
client.close()

html_soup = soup(html, "html.parser")

menus = html_soup.findAll('div',{'class':'col-sm-6 col-md-4'})

being_served = []

for menu in menus:
    dining_hall = str(menu.h3.text)
    menu = str(menu).lower()
    if fav_food in menu:
        being_served.append(dining_hall)
if being_served:
    being_served = list(set(being_served))
    location = " and ".join(being_served) if len(being_served) > 1 else being_served[0]
result = "Yay! That food is being served at " + location + " today!" if being_served[0] else "Sorry, that food is not being served today."

print(result)


        
