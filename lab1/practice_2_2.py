# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Also print the number of characters in the fist and last name.

first_name=input("Внеси име: ")
last_name=input("Внеси презиме: ")
full_name=first_name+" "+last_name

result=full_name[::-1]

print(first_name, "\n", last_name, "\n", result)
