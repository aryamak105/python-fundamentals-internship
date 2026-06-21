#check if number is < 100, then odd or even.

num = int(input("Enter a number: "))

if num < 100:
    if num % 2 == 0:
        print("EVEN number")
    else:
        print("Odd number")    
