#2 Write a python program to print the factorial of a given number.
# Example: 5 * 4 * 3* 2 * 1 = factoriel 5!

x = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, x + 1):
    factorial = factorial * i
print(f"The factorial of {x} is {factorial}")


#3 For list [2, 4, 55, 59,71,81, 87, 98, 99] calculate the sum and average of its elements.

numbers = [2, 4, 55, 59, 71, 81, 87, 98, 99]
total = sum(numbers)
average = total / len(numbers)
print(f"The sum of the list elements is: {total}")
print(f"The average of the list elements is: {average}")

#4 Reverse a given number using a loops. 123456 -> 654321

num = int(input("Enter a number to reverse: "))
reversed_num = 0    
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print(f"The reversed number is: {reversed_num}")

#5 Find the second largest number in a list.

numbers_list = [12,45,23,67,34,89,90,11,8,5654,2345234,23423,423,5324,5,235,2,352,35,24,234,2,456,547,56,785,8,567,567,56,45,45,34,3]
sorted_list = numbers_list.sort()
second_largest = numbers_list[-2]
print(f"The second largest number in the list is: {second_largest}")


#6 Create a list of all Kris Jenner’s (formerly Kardashian) kids first names (there should be 6 kids). Create a program that will print female kids’ proper full names.

kids = ["Maja", "Riki", "Vesna", "Miki", "Marija", "Zoki"]

for i in kids:
    if i in ["Maja", "Vesna", "Marija"]:
        print(f"{i} Kardashian")


# 7 Write a python program to read three numbers (a,b,c) and check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’.

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the divisor (c): "))
count = 0
for num in range(a, b):
    if num % c == 0:
        count += 1
print(f"There are {count} numbers between {a} and {b} that are divisible by {c}.")

#8 Write a Python program that accepts a string and calculate the number of digits and letters.

input_string = input("Enter a string: ")
digit_count = 0
letter_count = 0
for char in input_string:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1
print(f"Letters: {letter_count}, Digits: {digit_count}")

#9 Write a simple game that that asks the user to guess a secret number between 1 and 10. The game needs to prompt the user until hi/she/they guess the number. Number of attempts needs to be printed back with the success message.

import random
secret_number = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input("Guess the secret number between 1 and 10: "))
    attempts += 1
    if guess == secret_number:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break
    else:
        print("Wrong guess. Try again.")


####### Homework: Loops ########

#1 Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

even_digit_numbers = []
for num in range(100, 401):
    str_num = str(num)
    if all(int(digit) % 2 == 0 for digit in str_num):
        even_digit_numbers.append(str_num)

print(", ".join(even_digit_numbers))

#2 You have following list of fruits: ["apple", "tomato", "apple", "kiwi”, “apple", "orange", "banana", "apple", “kiwi” , “kiwi” , “kiwi”, “mango”]. Create a program that counts the occurrences of items in the given list.

'''
Example:
{ “banana” : 2,
“mango” : 1,
“kiwi” : 1
}
'''

fruits = ["apple", "tomato", "apple", "kiwi", "apple", "orange", "banana", "apple", "kiwi" , "kiwi" , "kiwi", "mango"]
fruit_count = {}
for x in fruits:
    if x in fruit_count:
        fruit_count[x] += 1
    else:
        fruit_count[x] = 1
print("Fruit occurrences:")
for fruit, count in fruit_count.items():
    print(f"{fruit}: {count}")

#3 Write a program that will check if given word is palindrome.

word = input("Enter a word to check if it's a palindrome: ")
if word == word[::-1]:
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")

#4 Convert given decimal to binary number using loops.

decimal_number = abs(int(input("Enter a decimal number to convert to binary: ")))
binary_number = ""
if decimal_number == 0:
    binary_number = "0"
while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number = decimal_number // 2
print(f"Binary representation: {binary_number}")