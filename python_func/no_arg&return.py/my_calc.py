def mycalc(a,b):
    p = a+b
    q = a-b
    r = a*b
    s = a/b
    return p,q,r,s
ans = mycalc(30,20)

for i in ans:
    print("Ans is",i)

