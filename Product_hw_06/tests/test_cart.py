import unittest
from product import Product
from cart import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        """Create basic objects for test."""
        self.product1 = Product("Milk", 22)
        self.product2 = Product("Phone", 800.00)
        
        self.cart = Cart()
        self.cart.add_product(self.product1, 2)
        # self.cart.add_product(self.product2)
        
    def test_add_product_and_success(self):
        """Checking the correct addition of the product"""
        self.cart.add_product(self.product2, 3)
        self.assertEqual(len(self.cart), 2)
        self.assertIn(self.product2, [item for item, _ in self.cart])
        self.assertEqual(self.cart.total(), 22 * 2 + 800.00 * 3)

    def test_add_product_invalid_type(self):
        """Checking for the correct product type."""
        with self.assertRaises(TypeError) as context:
            self.cart.add_product("Not product")
        self.assertEqual(str(context.exception), "Item must be a Product")

    def test_add_product_invalid_quantity(self):
        """Checking for the correct quantity type."""
        with self.assertRaises(TypeError) as context:
            self.cart.add_product(self.product2, "Invalid quantity")
        self.assertEqual(str(context.exception), "Quantity must be a number")
        
        with self.assertRaises(ValueError) as context:
            self.cart.add_product(self.product2, -1)
        self.assertEqual(str(context.exception), "Quantity must be positive")

    def test_remove_product(self):
        """Check the successful removal of the product"""
        self.cart.del_product(self.product1)
        self.assertEqual(len(self.cart), 0)
        # self.assertNotIn(self.product1, self.cart)
        self.assertNotIn(self.product1, [item for item, _ in self.cart])

    def test_remove_product_not_found(self):
        """Tests ValueError if the product is not in the catr."""
        with self.assertRaises(ValueError) as context:
            self.cart.del_product(self.product2)
        self.assertEqual(str(context.exception), "Product not found in the cart")

    def test_total(self):
        """Test total sum"""
        self.assertEqual(self.cart.total(), 22 * 2) 

    def tets_itegration(self):
        """Cart iteration check."""   
        items = list(self.cart)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0][0], self.product1)
        self.assertEqual(items[0][1], 2)

    def test_cart_merge(self):
        """Checking the merging of two baskets."""
        other_cart = Cart()
        other_cart.add_product(self.product2, 5)

        self.cart += other_cart
        items = list(self.cart)
        self.assertEqual(len(items), 2)
        self.assertIn(self.product2, [item for item, _ in self.cart])
        self.assertEqual(self.cart.total(), 22 * 2 + 800.00 * 5)

    def test_cart_merge_invalid(self):
        """Checking that the shopping cart is merged with an object of the wrong type"""
        with self.assertRaises(TypeError) as context:
            self.cart += "Not cart"
        self.assertEqual(str(context.exception), "Can only combine with another Cart")
    
    def test_str_representation(self):
        """Checking the text representation of the shopping cart"""
        cart_str = str(self.cart)
        self.assertIn("\nMilk: 2", cart_str)
        # self.assertIn("Phone: 2", cart_str)
        self.assertIn("\nTotal: 44", cart_str)


if __name__ == "__main__":
    unittest.main()


