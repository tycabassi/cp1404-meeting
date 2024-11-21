class Product:
    """Create a class on products and their price"""

    def __init__(self, name="", price=0.0):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}'


p1 = Product("Cheese", 12.50)
p2 = Product("Laptop", 912.95)
p3 = Product("Plant", 4.75)
print(p1, p2, p3)
