#myhome.py
#program to scrape data from myhome.e website
import csv
from bs4 import BeautifulSoup
import requests


retrieveTags=['PropertyListingCard__Price', 'PropertyListingCard__Address']

url = "https://www.myhome.ie/residential/mayo/property-for-sale?page=1"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#print (soup.prettify())


#listings = soup.find('div',class_='PropertyListingCard')
#print(listings)

with open('week3_myhome.csv', mode='w') as myhome_file:
    myhome_writer = csv.writer(myhome_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    listings = soup.findAll('div',class_='PropertyListingCard')

    for listing in listings:
        #print(listing)
 
        entrylist = []
        for tag in retrieveTags:
            entrylist.append(listing.find(class_=tag).text)
        myhome_writer.writerow(entrylist)
