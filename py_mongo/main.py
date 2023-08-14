from py_mongo.product import ProductCollection
from py_mongo.user import UserCollection

user_coll = UserCollection()
product_coll = ProductCollection()


# Insert
user_coll.insert_one({"name": "Alice", "age": 30})
user_coll.insert_one({"name": "Bob", "age": 21})
product_coll.insert_many([
    {"name": "Milk", "price": 13},
    {"name": "Bread", "price": 25},
    {"name": "Cucumber", "price": 5}
])

# Find
user = user_coll.find_one({"name": "Alice"})
print("User:", user)

users = user_coll.find()
print("Users:")
for user in users:
    print(user)

# Sort
products = product_coll.sort("price", direction=1)
print("Products (sorted by price ascending):")
for product in products:
    print(product)



#Delete
user_coll.delete_one({"name": "Alice"})
product_coll.delete_one({"price": 13})

#Drop
# user_coll.drop()
# product_coll.drop()
