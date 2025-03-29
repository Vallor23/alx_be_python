class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        print(f"{self.price * self.quantity} dollars")
        
product1 = product("Laptop", 1000, 2)
product1.calculate_total_price()
product2 = product("Smartphone", 500, 3)
product2.calculate_total_price()