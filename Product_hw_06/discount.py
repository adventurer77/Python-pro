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


class Discount:
    

    def __init__(self, value):
        if not isinstance(value, int | float):
            raise TypeError("Discount must be a number")
        if not 0 <= value <= 1:
            raise ValueError("Discount must be between 0 and 1")

        self.__value = value

    def discount(self):
        return self.__value


class GoldDiscount(Discount):
    def __init__(self, value=0.1):
        super().__init__(value)


class SilverDiscount(Discount):
    def __init__(self, value=0.2):
        super().__init__(value)

