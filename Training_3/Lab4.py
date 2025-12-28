#2 Write a Python program that for entered four random numbers you create lists of even and odd numbers lists. Print the list at the end.

even_numbers = []
odd_numbers = []
for _ in range(4):
    num = int(input("Enter a number: "))
    if num == 0:
        print("Zero is neither even nor odd.")
    elif num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("All numbers:", sorted(even_numbers + odd_numbers))

#3 Write Python program that for a given list of fruits ("apple", "banana", "cherry", "kiwi", "mango") will create new list with a fruits that contain the letter “a” and have less or equal to five characters.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
selected_fruits = [x for x in fruits if 'a' in x and len(x) <= 5]
print("Fruits with 'a' and <= 5 characters:", selected_fruits)

#4 You have a list of authorized users [“admin", “root” "john_doe", "jane_doe"] . You need to write a program that will check whether entered name is part of the authorized users and respond back with “Welcome <user>!”. If the user has administrative privileges than you need to additionally write “You have admin rights, don’t make career change actions!!!

authorized_users = ["admin", "root", "john_doe", "jane_doe"]
username = input("Enter your username: ")

if username in authorized_users:
    print(f"Welcome {username}!")
    if username in ["admin", "root"]:
        print("You have admin rights, don’t make career change actions!!!")
else:
    print("Unauthorized user.")

#5 '''You have following dictionary:
'''
student_scores = {
"Alice": 85,
"Jack": 80
"Bob": 45,
"Charlie": 92
}'''

#5 Write a program that will accept student name as input and will check if the student has passed the exam or not. Passing threshold is >=80 and you should also print the student result.

student_scores = {
    "Alice": 85,
    "Jack": 80,
    "Bob": 45,
    "Charlie": 92
}

student_name = input("Enter student name: ")
if student_name in student_scores:
    score = student_scores[student_name]
    if score >= 80:
        print(f"{student_name} has passed the exam with a score of {score}.")
    else:
        print(f"{student_name} has not passed the exam with a score of {score}.")
else:
    print("Student not found.")

#6 Write a program that will remove the duplicates of the following list: numbers_list = [5, -2, 3, 4, 4, 5, 9, 7, 8, 10, 5, 0, 8,-2, 3, -1]

numbers_list = [5, -2, 3, 4, 4, 5, 9, 7, 8, 10, 5, 0, 8, -2, 3, -1]
unique_numbers = list(set(numbers_list))
print("List after removing duplicates:", unique_numbers)



