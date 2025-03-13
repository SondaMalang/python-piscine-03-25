#!/usr/bin/python3

print("Please enter a number less than 25")
x = int(input())

while x < 25:
 x +=1
 print("Inside the loop, my variable is ",x)
 if (x==25):
  break
  
else:
 print("Error")
