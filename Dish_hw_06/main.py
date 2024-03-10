from dish import Dish 
from category import Category
from menu import Menu 
from discount import RegularDiscount 
from order import Order 


if __name__ == '__main__':
    try:
        main_dish1 = Dish("Tea", 10)
        main_dish2 = Dish('Pasta', 8)
        main_dish3 = Dish('Salad', 5)
        main_dish4 = Dish('Burger', 7)

        main_category1 = Category('Italian')
        main_category1.add_dish(main_dish1)
        main_category1.add_dish(main_dish2)
        main_category2 = Category('American')
        main_category2.add_dish(main_dish3)
        main_category2.add_dish(main_dish4)

        main_menu = Menu()
        main_menu.add_category(main_category1)
        main_menu.add_category(main_category2)
    
    
        main_discount = RegularDiscount(0.7)
        main_order = Order(main_discount)

        main_order2 = Order(main_discount)

        main_order.add_dish(main_dish1, 1)

        main_order2.add_dish(main_dish3, 1)
        main_order2.add_dish(main_dish4, 1)
     
        main_order += main_order2

        
        print(len(main_order))

        for i  in main_order:
            print(i)
        
        print(main_order[1])


        # print(main_order)
        # print(order.total_price())
    except IndexError:
        print("Index out of range. Please provide a valid index.")
    except Exception as e:
        print(e)
    
