from py_mongo.base import BaseMongo


class ProductCollection(BaseMongo):
    def __init__(self):
        super().__init__(db_name="mydatabase", collection_name="products")
