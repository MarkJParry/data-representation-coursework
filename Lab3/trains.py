import requests
import csv
from bs4 import BeautifulSoup
#import defusedxml

retrieveTags=['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainCode', 'TrainDate', 'PublicMessage', 'Direction' ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')

#print (soup.prettify())

listings = soup.findAll('objTrainPositions')

with open('week3_trains.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    listings = soup.findAll('objTrainPositions')

    for listing in listings:
        #print(listing)
        #print(listing.TrainLatitude.string)
        lat=float(listing.TrainLatitude.string)
        if lat < 53.4:
            entrylist = []
            for tag in retrieveTags:
                entrylist.append(listing.find(tag).string)
            train_writer.writerow(entrylist)