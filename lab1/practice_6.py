# Write a program that from entered “Name Fathers_Name Surname” you will extract the Father’s name.

Name=input("Внеси име, татково име и презиме: ")

result=Name.split(" ")[1]

print(result)