# Write a program that from entered “Name Fathers_Name Surname” you will extract the Father’s name.

Name=input("Внеси име: ")
Fathers_Name=input("Внеси татково име: ")
Surname=input("Внеси презиме: ")

full_name=Name+" "+Fathers_Name+" "+Surname

result=full_name.split(" ")[1]

print(result)