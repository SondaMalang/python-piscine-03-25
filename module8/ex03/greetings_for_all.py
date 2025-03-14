#!/usr/bin/python3
def greetings(text="Noble stranger"):
    if not text:
        print(f"Hello, {text}!")
    elif isinstance(text,str):
        print("Hello, ",text)
    elif not isinstance(text,str):
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
