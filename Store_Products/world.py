from products import Product
from store import Store
all_products = Product.all_products #** Created an alias for my Product's class list



#todo Create instances for the Product class
carrots = Product("Carrots", 100, "Vegatable")
# print(carrots)

avacados = Product("Avacados", 2, "Fruit")

beans = Product("Beans", 10, "Legume")

apples = Product("Granny-Smith", 2, "Fruit")

oranges = Product("Oranges", 2, "Fruit")


#todo Make sure products are put into a class list and test
print(all_products)


#** Testing newly assigned id's
print(carrots)
print(avacados) 
print(beans)




#todo create instance of Store class
walmart = Store("Walmart")


#** Testing add_products function
walmart.add_products(all_products) 
print(walmart.products[0])


#** Testing all other methods in store class
# walmart.inflation(.05)
# walmart.set_clearance("Fruit", .25)
# walmart.sell_products(2)

