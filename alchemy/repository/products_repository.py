from sqlalchemy import select
from alchemy.actions import ActionsOnTables
from alchemy.models.order_model import Order
from alchemy.models.product_model import Product


class ProductsRepository(ActionsOnTables):
    def __init__(self):
        super().__init__()

    def get_all(self):
        self.get_all_new(Product)

    def insert_one(self, product: Product):
        self.insert_new(product)

    def inner_join_with_new_column_total_price(self):
        sql_query = (select(Product.name, Product.price, Order.quantity,
                            (Product.price * Order.quantity).label('total_price'))
                     .join(Order))
        result = self._session.execute(sql_query).fetchall()
        for row in result:
            product_name, product_price, order_quantity, total_price = row
            print(f"Product: {product_name}, Price: {product_price}, Quantity: {order_quantity}, "
                  f"Total_Price: {total_price}")
