arr = []

for i in range(5):
    num = int(input("Enter number: "))
    arr.append(num)

# Ascending Order
for i in range(5):
    for j in range(i + 1, 5):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Ascending Order:", arr)

print("Descending Order:", end=" ")
for i in range(4, -1, -1):
    print(arr[i], end=" ")

