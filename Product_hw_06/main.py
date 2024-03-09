from product import Product
from cart import Cart
from discount import GoldDiscount, SilverDiscount
from order import Order
from user_exceptions import PriceError

if __name__ == '__main__':
    try:
        p1 = Product("Phone", 340)
        p2 = Product("Laptop", 1340)
        p3 = Product("Tablet", 540)
        p4 = Product("Smartwatch", 240)

        cart = Cart()
        cart.add_product(p1, 2)
        cart.add_product(p4, 1)
        cart2 = Cart()
        cart2.add_product(p2, 1)
        cart2.add_product(p3, 3)
        cart += cart2
        # print(cart)
        
        for i,q in cart:
            print(i,q)
        

        # discount = GoldDiscount()
        # order = Order("John", "Doe", cart, discount)
    
        


    except PriceError as pe:
        print(f"PriceError: {pe}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print("Done")