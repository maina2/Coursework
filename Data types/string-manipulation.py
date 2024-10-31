# String Manipulation

def string_info(s):
    print("Length:", len(s))
    print("Uppercase:", s.upper())
    print("Lowercase:", s.lower())
    print("First character:", s[0])
    print("Last character:", s[-1])

text = input("Enter a string: ")
string_info(text)