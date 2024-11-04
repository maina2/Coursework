def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)  # Output: 0 1 1 2 3 5 8 13 21 34

def find_max(a, b, c):
    return max(a, b, c)

print("The largest number is:", find_max(3, 7, 5))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5 is:", factorial(5))
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # Output: True
print(is_even(7))  # Output: False
def add(a, b):
    return a + b

result = add(3, 5)
print("The sum is:", result)
def greet_user(name):
    print(f"Hello, {name}! Welcome!")

greet_user("Alice")
def greet(name):
    print(f"Hello, {name}!")
