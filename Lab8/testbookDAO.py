#testbookDAO.py
from bookDAO import bookDAO

book = {
    'id':5,
    'title':'another book',
    'author':'yana',
    'price':1.99
}
book1 = {
    'id':5,
    'title':'yet another book',
    'author':'yet yana',
    'price':1.95
}

result = bookDAO.getAll()
print(result)
result = bookDAO.findByID(book1['id'])
print(result)
result = bookDAO.update(book1)
print(result)
result = bookDAO.findByID(book1['id'])
print(result)
result = bookDAO.delete(book1['id'])
print(result)
result = bookDAO.getAll()
print(result)