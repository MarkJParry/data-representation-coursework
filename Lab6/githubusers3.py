#This will pull only the  columns needed into the spreadsheet
#we are interested in their login and repository url

import json
from xlwt import *

#open the json file created in previous program githususers
#don't wnat to be pulling this down from web each time i test the program

filename = 'githubusers.json' 
with open(filename, 'r') as f: 
    data = json.load(f)


print(len(data))
print(data[0].keys())

header_column = ['login','repos_url']

#output to excel file
xlFile = "githubusers2.xls"
wb = Workbook()
ws = wb.add_sheet("Followers")

#add the header columns
row = 0
for idx, item in enumerate(header_column):
    #print(row,idx,item)
    ws.write(row,idx,item)

#add the data columns
#start the enumeration at 1
#this will loop through data showing each user
for row_idx,row in enumerate(data,1):
    #print(row_idx,row)
    #loop through the row to get the columns
    for col_idx,col_data in enumerate(header_column):
        #print(row_idx,col_idx,row[col_data])
        ws.write(row_idx,col_idx,row[col_data])


#save the workbook
wb.save(xlFile)