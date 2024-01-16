#Write a program that takes a number as input and prints whether it is positive, negative, or zero.

"""for i in range(10):
    number = eval(input("Enter a number: "))
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")"""

#Print the first 5 even numbers using a loop
        
for j in range(2, 13, 2):
    print(j)

#Create a list of numbers and print the square of each number

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in num:
    print(f"The square of {i} is {i**2}")

#Write a program that prints all prime numbers between 1 and 20

for a in range(1, 20): 
    b = int(a**0.5) + 1
    c = a % b
    print(f"The remenderof {a} % {b} is {c}")

    if c == 0:
        print("Not a prime number")
    else:
        print(f"{a} is a prime number")

#Given a string, count the number of vowels (a, e, i, o, u) in it.
    
stri = input("Enter a string: ")

count = 0
for l in stri:
    if l.lower() in "aeiou":
        count = count + 1

print(f"The number of vowels in {stri} is {count}")

#Given some number. Print "Even" if the number is even, and "Odd" if it's odd.

num1 = eval(input("Enter a number: "))

if num1 % 2 == 0:
    print(f"{num1} is Even")
else:
    print(f"{num1} is Odd")

#Write a program that prints random numbers from 1 to 10
    
from random import randint

a = randint(1, 10)

for i in range(a):
    print(i)

#Write a simple calculator
    
for i in range(5):
    var1 = eval(input("Enter number : "))

    if var1 != 0:
        print(var1)

#Write a program that calculates and prints the area of a rectangle. Take the length and width as input from the user.
        
length = eval(input("Enter the length of the Traiangle: "))
print()
width = eval(input("Enter the width of the Triangle: "))

area = length * width
print(area)

#Create a program that checks if a given year is a leap year.

year = eval(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or ( year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#Write a program to print the multiplication table of a given number up to 10.
    
multi_num = eval(input("Enter a number to see its multiplaction table: "))

for i in range(1, 11):
    print(f"the {multi_num} x {i} = {multi_num * i}")

#Create a program that takes a sentence as input and counts the number of words in it.
    
sentence = input("Enter a sentence: ")

word_count = len(sentence)
print(f"The number of words in {sentence}  is {word_count}")

# Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x, and 5x, each separated by three dashes, like below.

integer = eval(input("ENTER A NUMBER x: "))

print(f"{integer} --- {integer + integer} --- {integer + integer + integer} --- {integer + integer + integer + integer} --- {integer + integer + integer + integer + integer} ")

for i in range(4):
    print('*'*20)
    print('*' + " "*18 + '*')
    print('*' + " "*18 + '*')
    print('*'*20)

#Write a program that generates a random number, x, between 1 and 50, a random number y between 2 and 5, and computes x^y
    
x = randint(1, 50)
y = randint(2, 5)
print(x**y)

#write a program thats checks if a user is a child, Teen, Youth & adult based on the  age inputed. 

age = eval(input('ENTER YOUR AGE: '))

#1-12
#13-17
#18-30
#31-60

if age < 13:
    print(f"You are a Child")
elif age == 13 or age < 18:
    print(f"You are a Teen")
elif age == 18 or age < 31:
    print(f"You are a Youth")
elif age == 31 or age < 59:
    print(f"You are an Adult")
elif age == 60 or age <= 100:
    print(f"Mhen you are OLD")
else:
    print(f"Mhen you are not a human")