from user_exceptions import PriceError
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


class Product:
    """
    Клас для представлення продукту з назвою та ціною.

    Атрибути:
        name (str): Назва продукту.
        price (int | float): Ціна продукту.
    """
    def __init__(self, name: str, price: int | float):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")

        if not isinstance(price, int | float):
            raise TypeError("Price must be a number")
        if price <= 0:
            raise PriceError(price)

        self._name = name.strip()
        self._price = price

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value.strip()

    @property
    def price(self)-> int | float:
        return self._price
    
    @price.setter
    def price(self, value: int | float):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value <= 0:
            raise PriceError(value)
        self._price = value

    def __str__(self) -> str:
        return f"{self._name}: {self._price:.2f}"
