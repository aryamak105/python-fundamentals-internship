#simple calculator using switch case

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Result =", num1 + num2)
    case 2:
        print("Result =", num1 - num2)
    case 3:
        print("Result =", num1 * num2)
    case 4:
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid Choice")