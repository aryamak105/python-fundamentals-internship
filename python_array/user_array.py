import array as a1

arr_ele = a1.array('i',[])

n = int(input("Enter no of element:"))

for i in range(n):
    n1 = int(input("Enter value: "))
    arr_ele.append(n1)

print(arr_ele)

print(type(arr_ele))