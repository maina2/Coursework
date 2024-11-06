
class Vehicle :
    def __init__(self,brand,color):
        self.brand = brand
        self.color= color

        

    

class Car(Vehicle) :
    def __init__(self,speed,brand,color):
        super().__init__(brand,color)
        self.speed = speed
    
    def honk(self):
        print(f"The {self.color}, {self.brand}, going at {self.speed}kms/hr is now honcking ")

myCar = Car(300, color="Blue",brand="Benz")

myCar.honk()