#calculate avg. and print grade

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))
n4 = float(input("Enter number 4: "))
n5 = float(input("Enter number 5: "))

average = (n1 + n2 + n3 + n4 + n5) / 5

print("Average =", average)

if average < 50:
    print("Grade = F")
elif average < 60:
    print("Grade = D")
elif average < 70:
    print("Grade = C")
elif average < 80:
    print("Grade = B")
elif average < 90:
    print("Grade = A")
else:
    print("Grade = A+")