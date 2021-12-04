from flask import Flask, url_for, request, redirect, abort, jsonify
from bookDAO import bookDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')



@app.route('/')

def index():
    return "hello"




@app.route('/books',methods=['GET'])
def getAll():

    return jsonify(bookDAO.getAll())

# find By id
#curl http://127.0.0.1:5000/books/1 

@app.route('/books/<int:id>') 
def findById(id): 
    return jsonify(bookDAO.findByID(id))

# create
# curl -X POST -d "{\"id\":5,\"Title\":\"yab\", \"Author\":\"syaa\", \"Price\":1.23}" -H "content-type:application/json" http://127.0.0.1:5000/books 
@app.route('/books', methods=['POST']) 
def create(): 

    if not request.json: 
        abort(400) 

    book = { "id": request.json["id"], "title": request.json["title"], "author": request.json["author"], "price": request.json["price"]}


    return jsonify(bookDAO.create(book))

#update
# curl -X PUT -d "{\"title\":\"new Title\", \"price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/5 
@app.route('/books/<int:id>', methods=['PUT']) 
def update(id): 
    foundBook =  bookDAO.findByID(id)
    if foundBook == {}: 
        return jsonify({}), 404 
    currentBook = foundBook 
    if 'title' in request.json: 
        currentBook['title'] = request.json['title'] 
    if 'author' in request.json: 
        currentBook['author'] = request.json['author'] 
    if 'price' in request.json: 
        currentBook['price'] = request.json['price'] 
    bookDAO.update(currentBook)
    return jsonify(currentBook)

#delete
# curl -X DELETE http://127.0.0.1:5000/books/5 
@app.route('/books/<int:id>', methods=['DELETE']) 
def delete(id): 
    bookDAO.delete(id)
    return jsonify({"done":True})  

if __name__ == "__main__":
    app.run(debug=True)