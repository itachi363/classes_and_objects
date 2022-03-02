from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, customers_name):
        self.name = customers_name
        self.shopping_cart = ShoppingCart
        self.container = 0

    def add_product(self):
        self.shopping_cart == ShoppingCart.add_products

    def view_cart(self):
        self.container = 0
        while self.container < len(ShoppingCart):
            print(ShoppingCart[self.container])
            self.container = self.container + 1

