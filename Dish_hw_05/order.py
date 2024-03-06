import uuid
import datetime
from dish import Dish
from discount import Discount
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler("main_dish_05.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


class Order:
    def __init__(self, discount: Discount = None):
        
        self.id = uuid.uuid4()
        self.order_date = datetime.datetime.now()
        self.__dishes = []
        self.__quantities = []
        self.discount = discount

    def add_dish(self, item: Dish, quantity: int = 1):
            
            if not isinstance(item, Dish):
                logger.error("Dish must be a Dish object.")
                raise TypeError("Dish must be a Dish object.")
            if not isinstance(quantity, int | float):
                logger.error("Quantity must be a number.")
                raise TypeError("Quantity must be a number.")
            if quantity <= 0:
                logger.error("Quantity must be positive.")
                raise ValueError("Quantity must be positive.") 

            self.discount.discount()
            logger.info("Discount instance added to the Order: ")
            self.__dishes.append(item)
            logger.info("Dish instance added to the Order: ")
            self.__quantities.append(quantity)
            logger.info("Quantity instance added to the Order: ")
             

    def total_price(self):

        total = 0
        for dish, quantity in zip(self.__dishes, self.__quantities):
            total += dish.price * quantity
        return total * (1 - self.discount.discount() / 100)
    
    def __iadd__(self, other_order):
        
        if not isinstance(other_order, Order):
            raise TypeError("Can only combine with another Order")
        
        # self.id.extend(other_order.id)
        self.__dishes.extend(other_order.__dishes)
        self.__quantities.extend(other_order.__quantities)
        # self.discount.extend(other_order.discount)
        return self

    def __str__(self):

        items = '\n'.join([f'{dish.name} x {quantity} = {dish.price * quantity}' for dish, quantity in zip(self.__dishes, self.__quantities)])
        return f"Order: {self.id} \nDate: {self.order_date}\n{items}\nTotal price with discount: {self.total_price()}" 
        # return '\n'.join([f"{dish.name} x {quantity} = {self.total_price()}" for dish, quantity in zip(self.__dishes, self.__quantities)])