#!/usr/bin/python3

arr1 = [2, 8, 9, 48, 8, 22, -12, 2]

arr2 =[]


for i in range (len(arr1)): 
    arr2.append(arr1[i]+2)
    
print(f"Original array: {arr1}","\n",f"New array: {arr2}")
