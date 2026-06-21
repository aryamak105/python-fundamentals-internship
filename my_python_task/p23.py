#swap 2 numbers

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

temp = num1
num1 = num2
num2 = temp

print("After Swapping: ")
print("first number =" ,num1)
print("second number =",num2)