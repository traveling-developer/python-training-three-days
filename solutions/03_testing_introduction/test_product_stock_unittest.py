# test_product_inventory.py

import unittest
from unittest.mock import MagicMock
from codes.product_stock import get_product_quantity


class TestGetProductQuantity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a mock database connection
        cls.mock_db_connection = MagicMock()

        # Define the mock return values for different products
        cls.mock_db_connection.findProduct.side_effect = lambda product_id: {
            1: {"quantity": 50},
            2: {"quantity": 0}
        }.get(product_id, None)

    def test_get_product_quantity_available(self):
        product_id = 1
        expected_quantity = 50

        # Call the function and check the quantity
        quantity = get_product_quantity(self.mock_db_connection, product_id)
        self.assertEqual(quantity, expected_quantity)

    def test_get_product_quantity_out_of_stock(self):
        product_id = 2
        expected_quantity = 0

        # Call the function and check the quantity
        quantity = get_product_quantity(self.mock_db_connection, product_id)
        self.assertEqual(quantity, expected_quantity)

    def test_get_product_quantity_nonexistent_product(self):
        product_id = 99

        # Call the function and expect a ValueError for nonexistent product
        with self.assertRaises(ValueError):
            get_product_quantity(self.mock_db_connection, product_id)


if __name__ == "__main__":
    unittest.main()
