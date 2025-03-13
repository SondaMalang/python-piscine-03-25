#!/usr/bin/python3

print("Multiplication Table")
size = 10
row=0

while row <= size:
    print (f"Table of {row:<2}:", end="")
    column = 0
    while column <= size:
          print (f"{row*column:4}", end="")
          column+=1
    print()
    row +=1      

	
