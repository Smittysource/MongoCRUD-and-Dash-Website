# Implementation module for MongoCRUD
# David Smith
# SNHU CS-340
# Professor J. Sanford
# October 3, 2021

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId

class DatabaseConnector(object):

    """ CRUD operations for database in MongoDB """

    # Initialize class instance. 
    def __init__(self, server_ip: str, user: str, passwd: str, portnum: int, dbname: str, colname: str):

        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        
        # Connect to MongoDB using passed in username, password, server ip address,
        # port number, and database name.
        self.client = MongoClient('mongodb://%s:%s@%s:%i/%s' % (user,
                                                                    passwd,
                                                                    server_ip,
                                                                    portnum,
                                                                    dbname))

        # Create local variable to connect to database
        self.database = self.client[dbname]
        self.collection = self.database[colname]



# Create method to implement the C in CRUD.

    def create(self, data):

        # Ensure data to insert is not empty
        if data is not None:
                
            # Attempt to insert data into database
            try:

                # Check if data is in the correct format
                if type(data) is not dict:
                    raise Exception("Data parameter is not a dictionary")
            
                # Insert data into database, data should be dictionary
                insert_result = self.collection.insert_one(data)
                
                # Return response from database
                return insert_result.acknowledged
                
            # Throw exception if exception occurred
            except Exception as error:
                raise RuntimeError("There was an exception inserting into database") from error

        else:

            # Data is empty, throw exception
            raise Exception("Nothing to save, because data parameter is empty")



# Read method to implement the R in CRUD.

    def read(self, data):

        # Ensure data is not empty
        if data is not None:
        
            # Attempt to find data in database
            try:
                
                # Check if data is in the correct format
                if type(data) is not dict:
                    raise Exception("Data parameter is not dictionary")
                    
                # Return result of find command
                return self.collection.find(data,{"_id":False})   # data should be dictionary
                
            # Throw exception if operation failed
            except pymongo.errors.OperationFailure as operror:
                raise Exception("Operation failed.") from operror

        else:

            # Data is empty, throw exception
            raise Exception("Nothing to read, because data parameter is empty")
            
# Update method to implement the U in CRUD.

    def update(self, query, data):
        
        # Ensure query is not empty
        if query is None:
            raise Exception("Query parameter is empty")
        
        # Check if query is in correct format
        if type(query) is not dict:
            raise Exception("Query parameter is not a dictionary")
        
        # Check if data is not empty
        if data is None:
            raise Exception("Nothing to update as data parameter is empty")
        
        # Check if data is in correct format
        if type(data) is not dict:
            raise Exception("Data parameter is not a dictionary")
            
        return self.collection.update_many(query, {'$set': data})
            
# Delete method to implement the D in CRUD.
    
    def delete(self, query):
    
        # Ensure query is not empty
        if query is None:
            raise Exception("Query parameter is empty")
        
        # Check if query is in correct format
        if type(query) is not dict:
            raise Exception("Query parameter is not a dictionary")
        
        #Return result of API command
        return self.collection.delete_many(query)
