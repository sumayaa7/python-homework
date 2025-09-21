#ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")


#ValueError (input integer emas)
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: Not a valid integer!")


#ValueError (input integer emas)
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: Not a valid integer!")


#FileNotFoundError
try:
    with open("nofile.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("Error: File not found!")

#TypeError
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    res = float(a) + float(b)
except ValueError:
    raise TypeError("Inputs must be numbers!")

#Index error
nums = [1, 2, 3]
try:
    print(nums[5])
except IndexError:
    print("Error: Index out of range!")


#KeyboardInterrupt
try:
    num = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nError: Input cancelled by user!")


#ArithmeticError
try:
    res = 10 / 0
except ArithmeticError:
    print("Arithmetic Error occurred!")

#AttributeError
nums = [1, 2, 3]
try:
    nums.upper()
except AttributeError:
    print("Error: Attribute does not exist!")

#Append text
with open("test.txt", "a") as f:
    f.write("\nNew line added")
with open("test.txt") as f:
    print(f.read())

#Read last n lines
n = 2
with open("test.txt") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

#Store lines into list
with open("test.txt") as f:
    lines = f.readlines()
print(lines)

#Store into variable
with open("test.txt") as f:
    data = f.read()
print(data)

#Store into array (list)
with open("test.txt") as f:
    arr = [line.strip() for line in f]
print(arr)

#Find longest words
with open("test.txt") as f:
    words = f.read().split()
print(max(words, key=len))


#Count lines
with open("test.txt") as f:
    print(len(f.readlines()))

#Word frequency
from collections import Counter
with open("test.txt") as f:
    words = f.read().replace(",", " ").split()
print(Counter(words))


#File size
import os
print(os.path.getsize("test.txt"), "bytes")

#Write list to file
data = ["apple", "banana", "cherry"]
with open("out.txt", "w") as f:
    f.write("\n".join(data))


#Copy file
with open("test.txt") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())


#Random line
import random
with open("test.txt") as f:
    lines = f.readlines()
print(random.choice(lines))

#Check file closed
f = open("test.txt")
print(f.closed)   # False
f.close()
print(f.closed)   # True

#Remove newline characters
with open("test.txt") as f:
    lines = [line.strip() for line in f]
print(lines)


#Count words
with open("test.txt") as f:
    words = f.read().replace(",", " ").split()
print(len(words))

#Generate A–Z files
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(letter)

  #Alphabet with N letters per line
import string
n = 5
letters = string.ascii_uppercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write("".join(letters[i:i+n]) + "\n")
