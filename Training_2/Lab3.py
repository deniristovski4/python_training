#2 Write a Python program to sum of three given integers. However, if two given values are equal, sum will be zero.

a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
c=int(input("Enter number c: "))
if a == b and b == c and a == c:
    print("All numbers are equal")
elif a == b or b == c or a == c:
    print(0)
else:
    print(a + b + c)
#3 Write a Python program which represents grading system (points scored between 80 and 90 -> B, and so on).

points=int(input("Enter points: "))
if 90 <= points <= 100:
        print("A")
elif 80 <= points < 90:
    print("B")
elif 70 <= points < 80:
    print("C")
elif 60 <= points < 70:
    print("D")
elif 0 <= points < 60:
    print("F")
else:
    print("Invalid points")
#4 Write a Python program to find if number is just divisible by 7 and/or divisible by 5.

num=int(input("Enter a number: "))
if num == 0:
    print("Cannot devide with zero")
elif num % 7 == 0 and num % 5 == 0:
    print("Divisible by both 7 and 5")
elif num % 7 == 0:
    print("Divisible by 7")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 7 or 5")

#5 Write a program that will tell you if an input number is positive or not.

number=int(input("Enter a number: "))
if number > 0:
    print("The number is Positive")
elif number == 0:
    print("The number is Zero")
else:
    print("The number is Negative")

#6 Write a program if third letter of the name and forth letter of the surname of a full name (name _surname) are both consonants or vowels or mix.

full_name=input("Enter your full name: ")
full_name = full_name.split(" ")
name = full_name[0]
surname = full_name[1]
vowels = "aeiouAEIOU"
third_letter = name[2]
fourth_letter = surname[3]
if third_letter in vowels and fourth_letter in vowels:
    print("Both are vowels")
elif third_letter not in vowels and fourth_letter not in vowels:
    print("Both are consonants")
else:
    print("Mix")

##  Homework: Conditionals  ###

#7 Write a Python program that for a given year will calculate whether the year is Leap year or not. Check google/chatgpt on definition what is leap year.

year=int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")

#8 Write a program that for given two numbers and allowed operator (+, -, *, /) you will calculate (num1 operator num2) . If the given operator is not allowed, you should write a warning comment back.

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("Enter operator (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Cannot divide by zero")
else:
    print("Warning: Operator not allowed")