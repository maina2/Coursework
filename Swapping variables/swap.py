
def swap(a,b):
    a = a ^ b
    b = a ^ b
    a=  a ^ b

    return a,b

a = int(input("Enter your first value: "))
b = int(input("Enter your second value: "))

print(swap(a,b))


