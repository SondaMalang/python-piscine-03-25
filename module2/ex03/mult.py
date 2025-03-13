#!/usr/bin/python3

a =print("Welcome to the multiplier. Please enter your first number: ")
a = int(input())
print("Please enter your second number: ")
b = int(input())
 
mult = a * b

 
astr = str(a)
bstr = str(b)
multstr = str(mult)

if mult >0:
 print( astr + "*" + bstr + "=" + multstr + "\nThis number is positive")
elif mult <0:
 print(astr + "*" + bstr + "=" + multstr + "\nThis number is negative")
elif mult ==0:
 print(astr + "*" + bstr + "=" + multstr + "\nThis number is both positive and negative")
else:
 print("Please enter a number")

