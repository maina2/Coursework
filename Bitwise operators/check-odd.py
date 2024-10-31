def is_odd(x):
    return (x & 1) == 1

num = int(input("Enter an integer: "))
print("Is odd:", is_odd(num))
