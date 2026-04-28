class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)

    def buy_product(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f"Congrats! You bought {quantity} {product.name}")
                    return
                else:
                    print("Not enough stock available!")
                    return
        
        print("Product not found!")

shop = Shop()

p1 = Product("Laptop", 80000, 5)
p2 = Product("Mouse", 500, 10)

shop.add_product(p1)
shop.add_product(p2)

shop.buy_product("Laptop", 2)
shop.buy_product("Mouse", 15)
shop.buy_product("Keyboard", 1)