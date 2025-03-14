#!/usr/bin/python3  
import sys
def shrink(string):
    print(string[:8])
def enlarge(string):
    while len(string) <8:
        string += 'Z'
    print(string)
def main():
    for arg in sys.argv[1:]:
        if len(arg)>8:
            shrink(arg)
        elif len(arg)<8:
            enlarge(arg)
        else:
            print(arg,"\n")
if __name__ == "__main__" :
      main()                               