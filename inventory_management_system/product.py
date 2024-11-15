
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - Category: {self.category}, Price: ${self.price}, Stock: {self.stock_quantity}"
