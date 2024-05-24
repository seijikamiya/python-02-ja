class Vehicle():
    def __init__(self, model, make, year, price, discount=0):
        self.model = model
        self.make = make
        self.year = year
        self.price = price
        self.discount = discount

    def get_model(self):
        return self.model
    
    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year
    
    def get_price(self):
        return self.price
    
    def get_discount(self):
        return self.discount

    def set_model(self, model):
        self.model = model

    def set_make(self, make):
        self.make = make

    def set_year(self, year):
        self.year = year

    def set_price(self, price):
        self.price = price

    def set_discount(self, discount):
        self.discount = discount

    def display(self):
        print(
            f"----display vehicle info----\nmodel: {self.model}\nmake: {self.make}\nyear: {self.year}\nprice: {self.price}\ndiscount: {self.discount}"
        )