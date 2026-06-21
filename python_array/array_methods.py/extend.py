import array as arr

array_ele = arr.array('i', [ 10,20,30,40,50])
array_ele2 = arr.array('i', [45,78,89])

array_ele.extend(array_ele2)
print(array_ele)