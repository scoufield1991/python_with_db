import pymongo


my_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_name = my_client["mydatabase"]
