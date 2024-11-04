# test_product_inventory.py

import pytest
from unittest.mock import MagicMock
from codes.product_stock import get_product_quantity


# Fixture to set up a mock database connection
@pytest.fixture
def mock_db_connection():
    mock_db = MagicMock()
    # Define the mock return values for different products
    mock_db.findProduct.side_effect = lambda product_id: {
        1: {"quantity": 50},
        2: {"quantity": 0}
    }.get(product_id, None)
    return mock_db


def test_get_product_quantity_available(mock_db_connection):
    product_id = 1
    expected_quantity = 50

    # Call the function and check the quantity
    quantity = get_product_quantity(mock_db_connection, product_id)
    assert quantity == expected_quantity


def test_get_product_quantity_out_of_stock(mock_db_connection):
    product_id = 2
    expected_quantity = 0

    # Call the function and check the quantity
    quantity = get_product_quantity(mock_db_connection, product_id)
    assert quantity == expected_quantity


def test_get_product_quantity_nonexistent_product(mock_db_connection):
    product_id = 99

    # Call the function and expect a ValueError for nonexistent product
    with pytest.raises(ValueError, match="Product not found."):
        get_product_quantity(mock_db_connection, product_id)
