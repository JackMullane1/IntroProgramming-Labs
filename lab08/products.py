class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def purchase(self, count):
        self.quantity -= count

    
    def purchaseCost(self, count):
        return self.price * count
    

    def stockCheck(self, count):
        if self.quantity >= count:
            return True
        else:
            return False
        

