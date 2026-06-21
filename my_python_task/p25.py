#calculate sum of natural numbers.

num = int(input("enter a number: "))
total = 0

for i in range(1,num+1):
    total += i

print("Sum of natural numbers =",total)    