#!/usr/bin/python3

from pymongo import MongoClient
import os

class PowerStatisticDatabase:
    # Constructor for PowerStatisticDatabase class (db_name: str, collection_name: str, log_limit: int)
    # MONGO_CONNECTION_STRING is needed as an environment variable
    def __init__(self, db_name:str, collection_name:str, log_limit:int):
        self.client = MongoClient(os.environ.get('MONGO_CONNECTION_STRING'))
        self.log_limit = log_limit
        self.db = self.client[db_name]

        # If collection does not exist, create it
        if "statistics" not in self.db.list_collection_names():
            self.create_collection_statisics()
        

        # Use collection "Statistics"
        self.collection = self.db[collection_name]
        self.match_database_entries_to_log_limit()
    
    # Create collection "Statistics"
    def create_collection_statisics(self):
        self.db.create_collection(self.collection_name)
    
    # Insert document into collection "Statistics" (JSON Format)
    def insert_one(self, document):
        self.collection.insert_one(document)

    # Insert document into collection "Statistics" (JSON Format) and delete oldest entry if log_limit is reached
    def insert_one_with_limit(self, document):
        self.collection.insert_one(document)
        self.delete_oldest_entry()

    # Find all documents in collection "Statistics"
    def find_all_documents(self):
        return self.collection.find()
    
    # Find all documents in collection "Statistics" and return as list
    def find_all_documents_as_list(self):
        return list(self.collection.find())
    
    def get_all_dbs(self):
        return self.client.list_database_names()
    
    # delete oldest entry if log_limit is reached
    def delete_oldest_entry(self):
       if self.collection.count_documents({}) >= self.log_limit:
        self.collection.delete_one(self.collection.find_one())

    # delete all entries so it matches the log_limit
    def match_database_entries_to_log_limit(self):
        if self.collection.count_documents({}) >= self.log_limit:
            for i in range(self.collection.count_documents({}) - self.log_limit):
                self.collection.delete_one(self.collection.find_one())












# connect to db with connection string from env
# client = MongoClient(os.environ.get('MONGO_CONNECTION_STRING'))

# # use db
# db = client['db_restaurants']

# # db.[collection-name]
# collection = db["restaurants"]

# # find all documents in the collection and print the boroughs
# print(collection.distinct("borough"))

# # find all documents in the collection and print the boroughs
# collection_list = collection.find()

# # print all documents in the collection
# for col in collection_list:
#     print(col)
#     for m, v in col.items():
#         print(m + " " + str(v))
