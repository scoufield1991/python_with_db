from sqlalchemy.orm import relationship
from sqlalchemy import Column, INTEGER, VARCHAR, NUMERIC

from utilities.base import Base


class Product(Base):
    __tablename__ = 'products_test'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(25))
    price = Column(NUMERIC(5, 2))

    orders = relationship('Order', backref='product')

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}'
