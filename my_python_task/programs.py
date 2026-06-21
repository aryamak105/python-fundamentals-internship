#Q1:calculate area of rectangle

L = int(input("Enter length: "))
B = int(input("Enter breadth: "))
area = L*B
print("Area of rectangle =",area)

print("\n---------------------------------------------\n")

#Q2:Calculate area of square

L = float(input("Enter side length: "))
area =  L * L
print("Area os square =",area)

print("\n---------------------------------------------\n")

#Q3:calculate area of circle

pi = 3.14
radius = float(input("Enter radius: "))
area = pi * radius * radius
print("Area of circle =",area)

print("\n---------------------------------------------\n")

#Q4:Average of 5 numbers

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
n4 = float(input("Enter fourth number: "))
n5 = float(input("Enter fifth number: "))

average = (n1+n2+n3+n4+n5)/5
print("Average = ", average)

print("\n---------------------------------------------\n")

#Q5:calculate simple interest

p = float(input("Enter amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

simple_interest = (p * r * t)/100
print("Simple_interest = ",simple_interest)

print("\n---------------------------------------------\n")

#Q6:Take any three numbers and find squares & cubes

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

print("Square of", n1,"=", n1 ** 2)
print("cube of", n1,"=", n1 ** 3)

print("Square of", n2,"=", n2 ** 2)
print("cube of", n2,"=", n2 ** 3)

print("Square of", n3,"=", n3 ** 2)
print("cube of", n3,"=", n3 ** 3)

print("\n---------------------------------------------\n")


#Q7:Convert faherenheit to celsius

F = float(input("Enter temperature in fahreneit: "))

C = ((F-32)*5)/9

print("temperature in celsius = ",C)

print("\n---------------------------------------------\n")

#Q8:Check num is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("EVEN NUMBER")
else:
    print("ODD NUMBER")

print("\n---------------------------------------------\n")

#Q9:Check leap year or not

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100!= 0)
   print("Leap year")
else:
   print("Not a leap year")    




      
