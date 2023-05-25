import json
import os

class Product:
    def __init__(self):
        self.products = self.__load_all_products()

    def __load_all_products(self):
        try:
            with open(os.path.join(os.path.dirname(__file__), '..', 'data/products.json'), 'r') as file:
                product_data = json.load(file)
            return product_data
        except Exception as e:
            raise Exception('Products not fetched')

    def get_all_products(self):
        try:
            return self.products
        except Exception as e:
            raise Exception('Products not fetched')

    def get_product_by_id(self, id):
        try:
            for product in self.products:
                if product['id'] == id:
                    return product
            return None

        except Exception as e:
            raise Exception('Product details not fetched')