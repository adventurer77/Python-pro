from product import Product
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

class Cart:

    def __init__(self):
        self.__items = []
        self.__quantities = []

    def add_product(self, item: Product, quantity=1):
        if not isinstance(item, Product):
            raise TypeError("item must be a Product")
        if not isinstance(quantity, int | float):
            raise TypeError("Quantity must be a number")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.__items.append(item)
        self.__quantities.append(quantity)
  

    def total(self):
        return sum(item.price * quantity for item, quantity in zip(self.__items, self.__quantities))
    
    def __iadd__(self, other_cart):
        
        if not isinstance(other_cart, Cart):
            raise TypeError("Can only combine with another Cart")
        
        self.__items.extend(other_cart.__items)
        self.__quantities.extend(other_cart.__quantities)
        
        return self
        
        
    def __str__(self):
        items = "\n".join([f"{item.name}: {quantity}" for item, quantity in zip(self.__items, self.__quantities)])
        return f"Cart with: \n{items}\nTotal: {self.total()}"  