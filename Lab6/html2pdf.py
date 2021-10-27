#using a key with an api
import requests as rq
import json

#https://api.html2pdf.app/v1/generate?url=https://example.com&apiKey={your-api-key}
#set up url and file names
html2pdf_url = "https://api.html2pdf.app/v1/generate"
html_file = "../Lab5/carViewer3.html"
pdf_file = "carViewer3.pdf"



#add a minus sign after the first character before saving to github(git hub will invalidate key if found in file as a security measure)
my_api_key = '4-6ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
#remove the minus sign before using

#open the html file
infile = open(html_file,"r")
html = infile.read()
print(html)
infile.close()

#convert it to pdf using online html2pdf app
data = {'html':html,'apiKey':my_api_key}

response = rq.post(html2pdf_url, json=data)
print("status code is: ",response.status_code)

#save it to a pdf file
with open(pdf_file,"wb") as outfile:
    outfile.write(response.content)
    print("pdf file saved as ",pdf_file)






