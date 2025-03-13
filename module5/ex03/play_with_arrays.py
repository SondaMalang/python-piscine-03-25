#!/usr/bin/python3

arr1 = ([2, 8, 9, 48, 8, 22, -12, 2])
newarr = []

for x in arr1:
    if x>5: 
        newarr.append(x+2)

print(arr1,"\n",set(newarr))

