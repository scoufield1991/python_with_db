from alchemy.creating_deleting_tables import create_tables, drop_tables
from alchemy.models.order_model import Order
from alchemy.models.product_model import Product
from alchemy.repository.orders_repository import OrdersRepository
from alchemy.repository.products_repository import ProductsRepository

create_tables()

product_repo = ProductsRepository()
order_repo = OrdersRepository()

product_repo.insert_one(Product(id=1, name='potato', price=20.65))
product_repo.insert_one(Product(id=2, name='cucumber', price=15.91))
product_repo.insert_one(Product(id=3, name='milk', price=30.32))
product_repo.insert_one(Product(id=4, name='bread', price=10.01))
product_repo.insert_one(Product(id=5, name='butter', price=65.14))
order_repo.insert_one(Order(id=1, product_id=2, quantity=5))
order_repo.insert_one(Order(id=2, product_id=1, quantity=3))
order_repo.insert_one(Order(id=3, product_id=3, quantity=3))
order_repo.insert_one(Order(id=4, product_id=5, quantity=10))
order_repo.insert_one(Order(id=5, product_id=4, quantity=1))
product_repo.get_all()
order_repo.get_all()

product_repo.inner_join_with_new_column_total_price()



