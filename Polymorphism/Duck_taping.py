class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def animal_sound(animal):
    print(animal.speak())

# Testing duck typing
dog = Dog()
cat = Cat()
duck = Duck()

for animal in (dog, cat, duck):
    animal_sound(animal)  # Each will call the speak() method of its respective class

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # Overloading the + operator
    def __add__(self, other):
        combined_area = self.area() + other.area()
        return f"Combined area: {combined_area}"

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"

# Testing operator overloading
rect1 = Rectangle(4, 5)
rect2 = Rectangle(6, 3)

print(rect1 + rect2)  # Calls __add__ and combines the area

class CustomError(Exception):
    def __init__(self, message="This is a custom error"):
        self.message = message
        super().__init__(self.message)

def calculate(a, b, operator):
    try:
        if operator == "/":
            return a / b
        elif operator == "*":
            return a * b
        else:
            raise CustomError("Invalid operator!")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except CustomError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Testing error handling
calculate(10, 0, "/")  # ZeroDivisionError
calculate(10, 5, "+")  # CustomError
calculate(10, 2, "*")  # Valid, returns 20
