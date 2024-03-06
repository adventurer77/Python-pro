from user_exceptions import PriceError
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler("main_product_05.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


class Product:

    def __init__(self, name, price):
        if not isinstance(price, int | float):
            raise TypeError("Price must be a number")
        if price <= 0:
            raise PriceError(price)

        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"