#!/usr/bin/python3
import sys
import re

if len(sys.argv) !=2: 
  print("none\n")
  
else: 
  keyword = "z"
  text = sys.argv[1]
   
  matches  = re.findall(re.escape(keyword),text)
   
  if matches ==0:
    
    print("none")
    
  else: 
     matches = ''.join(matches)
     print(matches)