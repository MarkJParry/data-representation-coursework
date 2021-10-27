#http requestor
import requests as rq
#json
import json


#my server
url = "http://127.0.0.1:5000/cars"

#function to print out cars individually
def show_cars(data):    
    for car in data["cars"]:
        print(car)
    input("Press return to continue")


#get all the info
def refresh_url():
    response = rq.get(url)
    data = response.json()
    return data


data = refresh_url()
show_cars(data)




#create a car
new_car = {'reg':'08 C 1234','make':'Ford','model':'Galaxy','price':12324} 
response = rq.post(url, json=new_car) 
print (response.status_code)
print (response.text)
data = refresh_url()
show_cars(data)


#update a car
car_to_update = {'make':'Fjord','price':12324}
response = rq.put(url+"/08%20C%201234", json=car_to_update) 
print (response.status_code)
print (response.text)
data = refresh_url()
show_cars(data)

#delete a car
response = rq.delete(url+"/08%20C%201234") 
print (response.status_code)
print (response.text)
data = refresh_url()
show_cars(data)

