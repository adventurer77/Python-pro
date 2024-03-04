import Dish
import Category
import Menu
import Discount
import Order


if __name__ == '__main__':
    try:
        main_dish1 = Dish.Dish('Pizza', 10)
        main_dish2 = Dish.Dish('Pasta', 8)
        main_dish3 = Dish.Dish('Salad', 5)
        main_dish4 = Dish.Dish('Burger', 7)

        main_category1 = Category.Category('Italian')
        main_category1.add_dish(main_dish1)
        main_category1.add_dish(main_dish2)
        main_category2 = Category.Category('American')
        main_category2.add_dish(main_dish3)
        main_category2.add_dish(main_dish4)

        main_menu = Menu.Menu()
        main_menu.add_category(main_category1)
        main_menu.add_category(main_category2)
    
    
        main_discount = Discount.RegularDiscount(0.5)
        main_order = Order.Order(main_discount)

        main_order.add_dish(main_dish1, 1)
        print(main_order)
        # print(order.total_price())
    except Exception as e:
        print(e)

