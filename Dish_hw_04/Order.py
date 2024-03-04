import uuid
import Dish
import Discount
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler("main_dish_04.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


class Order:
    def __init__(self, discount: Discount):
        self.id = uuid.uuid4()
        self.__dishes = []
        self.__quantities = []
        self.discount = discount

    def add_dish(self, dish: Dish, quantity: int = 1):
            
            # if not isinstance(dish, Dish):
            #     logger.error("Dish must be a Dish object.")
            #     raise TypeError("Dish must be a Dish object.")
            if not isinstance(quantity, int | float):
                logger.error("Quantity must be a number.")
                raise TypeError("Quantity must be a number.")
            if quantity <= 0:
                logger.error("Quantity must be positive.")
                raise ValueError("Quantity must be positive.") 

            self.discount.discount()
            logger.info("Discount instance added to the Order: ")
            self.__dishes.append(dish)
            logger.info("Dish instance added to the Order: ")
            self.__quantities.append(quantity)
            logger.info("Quantity instance added to the Order: ")
             

    def total_price(self):

        total = 0
        for dish, quantity in zip(self.__dishes, self.__quantities):
            total += dish.price * quantity
        return total * (1 - self.discount.discount() / 100)

    def __str__(self):

        # return '\n'.join([f'{dish.name} x {quantity} = {dish.price * quantity}' for dish, quantity in zip(self.__dishes, self.__quantities)])
        return '\n'.join([f"{dish.name} x {quantity} = {self.total_price()}" for dish, quantity in zip(self.__dishes, self.__quantities)])