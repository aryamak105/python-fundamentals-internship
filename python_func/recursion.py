def countNumber(x):
    if x < 5:
        x = x +1
        print(x)
        countNumber(x)

countNumber(0)        