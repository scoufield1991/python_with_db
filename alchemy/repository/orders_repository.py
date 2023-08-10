from alchemy.actions import ActionsOnTables
from alchemy.models.order_model import Order


class OrdersRepository(ActionsOnTables):
    def __init__(self):
        super().__init__()

    def get_all(self):
        self.get_all_new(Order)

    def insert_one(self, order: Order):
        self.insert_new(order)
