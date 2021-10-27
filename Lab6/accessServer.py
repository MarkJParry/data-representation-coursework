#http requestor
import requests as rq
#json
import json
#excel
from xlwt import *

#my server
url = "http://127.0.0.1:5000/cars"


#get all the info
response = rq.get(url)
data = response.json()
print(data)
print(data.keys())

#print out cars individually
for car in data["cars"]:
    print(car)

filename = "cars.json"

#output data to a json file
with open(filename,"w") as outfile:
    json.dump(data,outfile,indent=4)

#output to excel file
xlFile = "cars.xls"
wb = Workbook()
ws = wb.add_sheet("Cars")

#add the header columns
header_column = ["make","model","price","reg"]
row = 0
for idx, item in enumerate(header_column):
    print(row,idx,item)
    ws.write(row,idx,item)

#add the data columns
row =1
#this will loop through cars showing each car
for row_idx,car in enumerate(data["cars"],1):
    print(row_idx,car)
    #loop through the car to get the columns
    for col_idx,col_data in enumerate(car):
        print(row_idx,col_idx,car[header_column[col_idx]])
        ws.write(row_idx,col_idx,car[header_column[col_idx]])
   # row += 1

#save the workbook
wb.save(xlFile)

