def dosum(a,b,c):
    d = a + b + c
    return d

def calculateAvg(total):
    per = total/300*100
    return per

totalmarks = dosum(85,65,74)
print("Total is ",totalmarks)

getper = calculateAvg(totalmarks)
print("% is",getper)
