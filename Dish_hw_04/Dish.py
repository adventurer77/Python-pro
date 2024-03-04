import uuid
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

class ErrorEnteringPrice(Exception):

    def __init__(self, message):

        self.message = message
        # self.product_name = product_name 

    def __str__(self):
        return f"{self.message}. "
# , self.name \nProduct:{self.product_name}

class Dish:
    def __init__(self,name: str, price):

        if not isinstance(name,str):
            logger.error("Name must be a string.")
            raise TypeError("Name must be a string.")
        if not isinstance(price,int | float):
            logger.error("Price must be a number.")
            raise TypeError("Price must be a number.")
        if price <= 0:
            logger.error("The price cannot be less than or equal to zero")
            raise ErrorEnteringPrice("The price cannot be less than or equal to zero")
        
        self.name = name
        self.price = price
        self.__id = uuid.uuid4()
        logger.info(f"Dish instance created with id: {self.__id}")

    def __str__(self):

        return f'{self.name}: {self.price}'