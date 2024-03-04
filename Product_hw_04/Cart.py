import uuid
import logging
import Product


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler("main_product_04.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


class CartLimitError(Exception):

    def __init__(self, message, limit):

        self.message = message
        self.limit = limit

    def __str__(self):

        return f'{self.message}. Limit: {self.limit}'

class Cart:

    def __init__(self,max_products_limit=5):

        self.__products = []
        self.__quantity = []
        self.max_products_limit = max_products_limit

    def add_product(self, product: Product, quantity = 1):

        # if not isinstance(product,Product.Product(str,int|float)):
        #     logger.error("Product must be a Product object.")
        #     raise TypeError("Product must be a Product object.")
        if not isinstance(quantity, int | float):
            logger.error("Quantity must be a number.")
            raise TypeError("Quantity must be a number.")
        if quantity <= 0:
            logger.error("Quantity must be positive.")
            raise ValueError("Quantity must be positive.")
        if len(self.__products) >= self.max_products_limit:
            logger.error('Cart is full', self.max_products_limit)
            raise CartLimitError('Cart is full', self.max_products_limit)
        
        self.__products.append(product)
        logger.info(f"Product instance added to the cart")
        self.__quantity.append(quantity)
        logger.info(f"Quantity instance added to the cart")

    def remove_product(self, product: Product, quantity: int | float = 1):

        if product in self.__products:
            index = self.__products.index(product)
            self.__quantity[index] -= quantity
            if self.__quantity[index] <= 0:
                del self.__products[index]
                del self.__quantity[index]

    def total(self):

        total = 0
        for product, quantity in zip(self.__products, self.__quantity):
            total += product.price * quantity
        return total

    def __str__(self):

        if not self.__products:
            return 'Cart is empty'
        return '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
                             zip(self.__products, self.__quantity))) +\
               f'\nTotal: {self.total()} UAH'







# try:
        

#         cart = Cart()
#         cart.add_product(product1, 2)
#         # cart.add_product(product2,1)
#         # cart.add_product(product3, 3)
#         # cart.add_product(product1, 2)
#         # cart.add_product(product1, 2)
#         # cart.add_product(product1, 2)
#         print(cart)
# except Exception as e:
#         print(e)