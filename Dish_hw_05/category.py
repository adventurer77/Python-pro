from dish import Dish
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



class Category:
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)
        logger.info(f"Dish instance added to the Category: {self.name}")

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.__dishes))


class Menu:
    def __init__(self):
        self.__categories = []

    def add_category(self, category: Category):
        self.__categories.append(category)
        logger.info(f"Category instance added to the Menu.")

    def __str__(self):
        return '\n'.join(map(str, self.__categories))