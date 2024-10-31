def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
a, b = swap(a, b)
print("After swapping:", a, b)
