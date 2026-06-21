#check number is zero, positive and negative

n=int(input("Enter the number : "))

if n >= 0:
    if n == 0:
        print(f"The number is equal {n}")
    else:
        print(f"The number is postive {n} ")
else:
    print(f"The number is negative {n}")