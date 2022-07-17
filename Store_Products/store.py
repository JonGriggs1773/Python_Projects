from products import Product



class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_products(self, products_list):
        for items in range(len(products_list)):
            self.products.append(products_list[items])
        return self

    def sell_products(self, id_number):
        for food in range(len(self.products)- 1):
            if self.products[food].id == id_number:
                self.products.pop(food)
        print(self.products)
        return self

    def inflation(self, percent_increase):
        for food in self.products:
            print(food.price)
            food.update_price(percent_change, True)
            print(food.price)

    def set_clearance(self, category, percent_discount):
        for food in self.products:
            if food.category == category:
                food.update_price(percent_discount, False)
                print(food.price)
