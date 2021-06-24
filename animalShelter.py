from pymongo import MongoClient, cursor

import json


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user: str, pw: str):

        # Initializing the MongoClient. This helps to 

        # access the MongoDB databases and collections. 

        self.client = MongoClient('mongodb://%s:%s@localhost:43345/AAC' % (user, pw))

        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.

    def create(self, data: dict) -> bool:
        """Insert a document based on a provided dict"""
        if data is not None:

            result = self.database.animals.insert(data)  # data should be dictionary            
            print(result)
            if result is not None:
                return True
            else:
                return False
        else:

            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.

    def read(self, data: dict) -> cursor:
        """Find a document based on a provided dict"""
        if data is not None:

            return self.database.animals.find(data, {"_id": False})  # data should be a dictionary

        else:

            raise Exception("Nothing to find because data parameter is empty")

    # Create method to implement the U in CRUD

    def update(self, lookup: dict, new_data: dict) -> json:
        """Find a document to match first argument and update with second"""
        if lookup and new_data is not None:

            return json.dumps(self.database.animals.update(lookup, {"$set": new_data}))

        else:

            raise Exception("Nothing to update because one of the arguments are empty")

    # Create method to implement the D in CRUD

    def delete(self, data: dict) -> json:
        """Delete the document based on the argument given"""
        if data is not None:

            return json.dumps(self.database.animals.remove(data))

        else:

            raise Exception("Nothing to delete because the data was not provided")
