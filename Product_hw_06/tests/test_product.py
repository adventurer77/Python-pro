import unittest
from product import Product
from user_exceptions import PriceError


class TestProduct(unittest.TestCase):
    def test_create_product_valid(self):
        # Check the correct creation of the object.
        product = Product("Phone", 340.10)
        self.assertEqual(product.name, "Phone")
        self.assertEqual(product.price, 340.10)

    def test_create_product_invalid_name(self):
        # Checking for an incorrect name
        with self.assertRaises(ValueError) as context:
            Product("", 340.10)
        self.assertEqual(str(context.exception), "Name must be a non-empty string.")

    def test_create_product_invalid_price(self):
        # Checking for an incorrect price
        with self.assertRaises(PriceError) as context:
            product = Product("Phone", -12)
        self.assertEqual(
            str(context.exception), "Price -12 is invalid. Price must be positive."
        )

    def test_create_product_zero_price(self):
        # Перевірка створення продукту з нульовою ціною
        with self.assertRaises(PriceError) as context:
            Product("Phone", 0)
        self.assertEqual(
            str(context.exception), "Price 0 is invalid. Price must be positive."
        )

    def test_set_valid_name(self):
        # Checking the set correct name
        product = Product("Phone", 340.10)
        product.name = "Milk"
        self.assertEqual(product._name, "Milk")

    def test_set_invalid_name(self):
        # Checking the set incorrect name
        product = Product("Phone", 340.10)
        with self.assertRaises(ValueError) as context:
            product.name = ""
        self.assertEqual(str(context.exception), "Name must be a non-empty string.")

    def test_set_valid_price(self):
        # Checking the set correct price
        product = Product("Phone", 340.10)
        product.price = 22.21
        self.assertEqual(product._price, 22.21)

    def test_set_invalid_price(self):
        # Checking the set incorrect price
        product = Product("Phone", 340.10)
        with self.assertRaises(PriceError) as context:
            product.price = -2
        self.assertEqual(
            str(context.exception), "Price -2 is invalid. Price must be positive."
        )

    def test_invalid_name_with_whitespace(self):
        # Перевірка назви, що складається лише з пробілів
        with self.assertRaises(ValueError) as context:
            Product("   ", 100)
        self.assertEqual(str(context.exception), "Name must be a non-empty string.")

    def test_str_representation(self):
        # We check __str__ method
        product = Product("Phone", 340.10)
        self.assertEqual(str(product), "Phone: 340.10")


if __name__ == "__main__":
    unittest.main()
