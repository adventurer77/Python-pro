import datetime
import uuid
from cart import Cart
from discount import Discount
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler("main_product_06.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


class Order:

    def __init__(self, first_name: str, last_name: str, cart: Cart, discount: Discount = None):
        self.first_name = first_name
        self.last_name = last_name
        self.order_id = uuid.uuid4()
        self.order_date = datetime.datetime.now()
        self.cart = cart
        self.discount = discount


    def price(self):
        total = self.cart.total()
        return total * (1 - self.discount.discount()) if self.discount else total
    

    def __str__(self):
        return f"Order: {self.order_id}\nDate: {self.order_date}\n{self.cart}\nTotal: {self.price()}"
      