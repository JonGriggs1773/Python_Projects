class Product:
    all_products = []
    inventory = 1
    def __init__(self, name, price, category):
        self.id = Product.inventory
        self.name = name
        self.price = price
        self.category = category
        Product.all_products.append(self)
        Product.inventory += 1

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price * (1 + percent_change)
        else:
            self.price = self.price * (1 - percent_change)
        return self

    def print_info(self):
        print(self.name)
        print(self.category)
        print(self.price)
        return self





