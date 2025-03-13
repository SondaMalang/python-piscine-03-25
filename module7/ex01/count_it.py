#!/usr/bin/python3
import sys


if len(sys.argv) <2: 
  print("none\n")
  
else: 
   
   pars = sys.argv[1:]
   count = len(pars)
   print("parameters: ",count)   

   for arg in sys.argv[1:]:
    count2 =len(arg)
    print(arg,":",count2)


