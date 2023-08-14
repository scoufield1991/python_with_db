from py_mongo.client_for_mongo import my_client


class BaseMongo:
    def __init__(self, db_name, collection_name):
        self.client = my_client
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def find_one(self, filter=None):
        return self.collection.find_one(filter)

    def find(self, filter=None):
        return self.collection.find(filter)

    def delete_one(self, filter):
        return self.collection.delete_one(filter)

    def sort(self, key_or_list, direction=None):
        return self.collection.find().sort(key_or_list, direction)

    def drop(self):
        return self.collection.drop()
