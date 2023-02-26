#python lib code
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username="aacuser",password="password"):
        # Initializing the MongoClient. This helps to 
        #self.client = MongoClient('mongodb://localhost:54110')
        # access the MongoDB databases and collections.
        if username and password:
             self.client = MongoClient('mongodb://%s:%s@localhost:54110/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        else:
            self.client = MongoClient('mongodb://localhost:54110')
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary  
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD
    def read_all(self,data):
        cursor = self.database.animals.find(data, {'_id':False} )
        return cursor

    def read(self,data):
        return self.database.animals.find_one(data)
    
# Create method to implement the U in CRUD
    def update(self, data, updated):
        
            answer = self.database.animals.update_many(data, {'$set': updated})
            return answer.matched_count
# Create method to implement the D in CRUD  
    def delete(self, data):
        answer = self.database.animals.delete_many(data)
        return answer.deleted_count
