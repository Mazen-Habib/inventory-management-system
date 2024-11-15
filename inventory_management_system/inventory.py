
from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def view_products(self):
        for product in self.products:
            print(product)

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def remove_product(self, product_id):
        product = self.find_product(product_id)
        if product:
            self.products.remove(product)
            return True
        return False
