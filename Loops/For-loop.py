# numbers = [10, 20, 30, 40, 50]
# total = 0

# for numero in numbers:
#     total = total+ numero
# print("Total sum:", total)

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# n = int(input("Enter a positive integer: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print("Sum of the first", n, "natural numbers is:", total)

# Count Vowels in a String
text = str(input("Enter the desired string: "))
vowels= "aeiouAEIOU"
count= 0

for vowel in text :
    if vowel in vowels :
        count+= 1
        print("the number of vowels are::  ",  vowel)
print("the number of vowels is::",count )



