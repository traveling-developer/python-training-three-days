def get_product_quantity(db_connection, product_id):
    """Fetches the quantity of a product from the inventory database."""
    product = db_connection.findProduct(product_id)

    if product is None:
        raise ValueError("Product not found.")

    quantity = product['quantity']
    return quantity
