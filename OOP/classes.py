
class Car :
    def __init__(self,make,price,speed,color,year):
        self.make= make
        self.price = price
        self.speed = speed
        self.color = color
        self.year = year
    
    def display_details(self):
        print(f"This is a {self.color}, {self.make}, {self.year}")
    
    def price_tag(self):
        print(f"The {self.make}, goes for {self.price} Dollars ")

    def current_speed(self):
        print(f"You are currently driving at {self.speed} kms per hour")



first_car = Car("Benzo",30000,200,"Black",2020)

first_car.display_details()
first_car.price_tag()
first_car.current_speed()