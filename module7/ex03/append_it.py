#!/usr/bin/python3
import sys
def main():
    if len(sys.argv)==1:
        print("none\n")

    else:
        for arg in sys.argv[1:]:
            if not arg.endswith("ism"):
                print(arg+"ism")   

if __name__ == "__main__":      
 main()           