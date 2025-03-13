#!/usr/bin/python3
import sys

if len(sys.argv)==2:
 word = input("What was the parameter? ")
 if word == sys.argv[1]:
  print("Good job!\n")
 else:
  print("Nope, sorry...")
 
else: 
 print("none","\n")