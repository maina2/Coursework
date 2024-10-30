
# Basic Bitwise Operations
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)


# Bitwise NOT Operation
def bitwise_not(x):
    return ~x

num = int(input("Enter an integer: "))
print("NOT:", bitwise_not(num))
print("Binary format:", bin(bitwise_not(num)))


# Left and Right Shift Operations
x = int(input("Enter an integer: "))
left_shift = x << 2
right_shift = x >> 2

print("Left Shift:", left_shift, "Binary:", bin(left_shift))
print("Right Shift:", right_shift, "Binary:", bin(right_shift))


# Check if a Number is Odd or Even Using Bitwise AND
def is_odd(x):
    return (x & 1) == 1

num = int(input("Enter an integer: "))
print("Is odd:", is_odd(num))
