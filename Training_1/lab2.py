#1.2 Try following mathematical operators inside python environment: addition, subtraction, multiplication, division, floor division, modulus, exponentiation.

x=2+3
y=5*6
z=15-8
m=12/4
n=7%3
k=16//5
p=2**3

print(x, y, z, m, n, k, p)

#2.1 Write a Python program which accepts the radius of a circle from the user and compute the area.

radius=input("Внеси радиус: ")
Area=3.14*float(radius)**2

print("Area =", Area)

#2.2 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Also print the number of characters in the fist and last name.

first_name=input("Внеси име: ")
last_name=input("Внеси презиме: ")
full_name=first_name+" "+last_name

result=full_name[::-1]

print(first_name, "\n", last_name, "\n", result)

#3 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n=input("Внеси број: ")

nn=n+n
nnn=n+n+n

result=int(n)+int(nn)+int(nnn)

print(result)

#4 Write a Python program that accepts an numbers of days (integer ) and computes the total number of seconds for the specified days value.

days=input("Внеси број на денови: ")

seconds=int(days)*24*60*60

print(seconds)

#5 Write a program where in following text will replace North Macedonia with Macedonia without allowing any extra spaces:
# “North Macedonia is a member of NATO, the Council of Europe, the World Bank, OSCE, CEFTA, BSEC and the WTO. Since 2005, it has also been a candidate for joining the European Union. North Macedonia is an upper-middle-income country by the World Bank's definitions and has undergone considerable economic reform since its independence in developing an open economy. It is a developing country with a very high Human Development Index and low income inequality; and provides social security, a universal health care system, and free primary and secondary education to its citizens.”

NMK="North Macedonia is a member of NATO, the Council of Europe, the World Bank, OSCE, CEFTA, BSEC and the WTO. Since 2005, it has also been a candidate for joining the European Union. North Macedonia is an upper-middle-income country by the World Bank's definitions and has undergone considerable economic reform since its independence in developing an open economy. It is a developing country with a very high Human Development Index and low income inequality; and provides social security, a universal health care system, and free primary and secondary education to its citizens."

MK=NMK.replace("North Macedonia", "Macedonia")

print(MK)

#6 Write a program that from entered “Name Fathers_Name Surname” you will extract the Father’s name.

Name=input("Внеси име, татково име и презиме: ")

result=Name.split(" ")[1]

print(result)