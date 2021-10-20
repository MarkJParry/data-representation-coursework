#!flask/bin/python
from flask import Flask 

#Get the app server to be able to serve static pages
app = Flask(__name__, 
            static_url_path='', 
            static_folder='../')

#app = Flask(__name__) 

@app.route('/') 
def index(): 
    return "Hello, World!" 
    
if __name__ == '__main__' : app.run(debug=True)



