import mysql.connector
import configDB as cfg
class BookDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=       cfg.mysql['host'],
        user=       cfg.mysql['username'],
        password=   cfg.mysql['password'],
        database=   cfg.mysql['database']
        )
    
            
    def create(self, book):
        #print(values)
        cursor = self.db.cursor()
        sql="insert into book (id, title, author, price) values (%s,%s,%s,%s)"
        values = [book['id'],book['title'],book['author'],book['price']]
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from book where id = %s"
        values = [id]

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, book):
        cursor = self.db.cursor()
        sql="update book set title= %s,author=%s, price=%s  where id = %s"
        values = [book['title'],book['author'],book['price'],book['id']]
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from book where id = %s"
        values = [id]

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','title','author', "price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
bookDAO = BookDAO()