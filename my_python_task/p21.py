#find smallest number using logical operator

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a <= c and a <= b:
    print(a)
elif b <= c and b <= a:
    print(b)
else:
    print(c)        
   