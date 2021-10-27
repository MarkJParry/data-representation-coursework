#using a key with an api
import requests as rq
import json


#set up url and file names
github_url = "https://api.github.com/repos/MarkJParry/privaterepo"
#html_file = "../Lab5/carViewer3.html"
json_file = "privateone.json"



#add a minus sign after the first character before saving to github(git hub will invalidate key if found in file as a security measure)
my_api_key = 'g-hp_y5qUTCHy9cechpV7v48WJLTPdEpNsx1sq43i'
#remove the minus sign before using

response = rq.get(github_url,auth=('token', my_api_key))
jresponse = response.json()
print(jresponse)

with open(json_file, "w") as outfile:
    json.dump(jresponse, outfile, indent=4)






