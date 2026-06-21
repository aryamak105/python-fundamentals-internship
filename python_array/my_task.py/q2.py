# Max and Min
arr = []

for i in range(5):
    num = int(input("Enter number: "))
    arr.append(num)

max_num = arr[0]
min_num = arr[0]

for i in range(1, 5):
    if arr[i] > max_num:
        max_num = arr[i]

    if arr[i] < min_num:
        min_num = arr[i]

print("\nMaximum Number:", max_num)
print("Minimum Number:", min_num)