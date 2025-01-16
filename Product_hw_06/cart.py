from product import Product
from iter_cart import IterCart
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


class Cart:

    def __init__(self):
        self.__items = []
        self.__quantities = []

    def add_product(self, item: Product, quantity=1):
        if not isinstance(item, Product):
            raise TypeError("Item must be a Product")
        if not isinstance(quantity, (int, float)):
            raise TypeError("Quantity must be a number")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if item in self.__items:
            index = self.__items.index(item)
            self.__quantities[index] += quantity
        else:
            self.__items.append(item)
            self.__quantities.append(quantity)

    def del_product(self, item: Product):
        if item not in self.__items:
            raise ("Product not found in the cart")

        index = self.__items.index(item)
        del self.__items[index]
        del self.__quantities[index]

    def total(self):
        return sum(
            item.price * quantity
            for item, quantity in zip(self.__items, self.__quantities)
        )

    def __iadd__(self, other_cart):

        if not isinstance(other_cart, Cart):
            raise TypeError("Can only combine with another Cart")

        self.__items.extend(other_cart.__items)
        self.__quantities.extend(other_cart.__quantities)

        return self

    def __getitem__(self, index):
        return  self.__items[index], self.__quantities[index]

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        return IterCart(self.__items, self.__quantities)

    def __str__(self):
        items = "\n".join(
            [
                f"{item.name}: {quantity}"
                for item, quantity in zip(self.__items, self.__quantities)
            ]
        )
        return f"Cart with: \n{items}\nTotal: {self.total()}"
