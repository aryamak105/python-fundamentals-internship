#find smallest num

a =  int(input("enter first number: "))
b = int(input("enter second number: "))

smallest = a if a < b else b

print("smallest number = ",smallest)