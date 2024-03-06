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

class Discount:
    def __init__(self, value):

        if not isinstance(value, float | int):
            logger.error("Value must be a float.")
            raise ValueError("Value must be a float.")
        if not 0 <= value <= 1:
            logger.error("Value must be between 0 and 1.")
            raise ValueError("Value must be between 0 and 1.")

        self._value = value

    def discount(self):
        logger.error("Subclass must implement this method")
        raise NotImplementedError("Subclass must implement this method")


class RegularDiscount(Discount):

    def __init__(self, value=0.2):
        super().__init__(value)

    def discount(self):
        return self._value


class SilverDiscount(Discount):

    def __init__(self, value=0.5):
        super().__init__(value)

    def discount(self):
        return self._value


class GoldDiscount(Discount):

    def __init__(self, value=0.8):
        super().__init__(value)

    def discount(self):
        return self._value