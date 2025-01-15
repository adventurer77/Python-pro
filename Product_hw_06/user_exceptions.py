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


class PriceError(Exception):
    """
    Користувацький виняток для некоректної ціни.
    
    Атрибути:
        price (int | float): Некоректна ціна, що спричинила виняток.
        message (str): Повідомлення про помилку.
    """
    def __init__(self, price: int | float):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be an integer or float.")
        if price <= 0:
            message = f"Price {price} is invalid. Price must be positive."
        else:
            message = f"Price {price} is invalid."
        
        self.price = price
        self.message = message
        super().__init__(self.message)