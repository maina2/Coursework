# Identify Data Types

values = [42, 3.14, "hello", [1, 2, 3], {"name": "Alice", "age": 25}]
for value in values:
    print(f"The type of {value} is {type(value)}")







# String Manipulation

def string_info(s):
    print("Length:", len(s))
    print("Uppercase:", s.upper())
    print("First character:", s[0])
    print("Last character:", s[-1])

text = input("Enter a string: ")
string_info(text)
