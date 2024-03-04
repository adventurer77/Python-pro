import Product
import Cart




if __name__ == '__main__':

    try:
        
        main_product1 =  Product.Product('Milk', 12)
        main_product2 =  Product.Product('Bread', 10)
        main_product3 =  Product.Product('Eggs', 20)

        main_cart = Cart.Cart()
        main_cart.add_product(main_product1,1) 
        main_cart.add_product(main_product2,2)
        main_cart.add_product(main_product3,3)
        print(main_cart)
    except Exception as e:
        print(e)

    