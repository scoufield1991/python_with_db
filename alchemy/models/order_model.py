from sqlalchemy import Column, INTEGER, ForeignKey

from utilities.base import Base


class Order(Base):
    __tablename__ = 'orders_test'
    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey('products_test.id'))
    quantity = Column(INTEGER)

    def __str__(self):
        return f'id: {self.id}, product_id: {self.product_id}, quantity: {self.quantity}'
