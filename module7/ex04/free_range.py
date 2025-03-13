#!/usr/bin/python3
import sys
import re

if len(sys.argv) !=3: 
  print("none\n")
  
else: 
   nums =[]
   arg1 = int(sys.argv[1])
   arg2 = int(sys.argv[2])
   for i in range(arg1,(arg2+1)):
    nums.append(i) 
   print(nums)