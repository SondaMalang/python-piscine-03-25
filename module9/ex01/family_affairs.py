#!/usr/bin/python3

def find_the_redheads(a):
    
   return list(filter(lambda name: a[name] == "red", a.keys()))


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))

