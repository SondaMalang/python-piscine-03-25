#!/usr/bin/python3

def array_of_names(persons):
    full_name = []
    for k,v in persons.items():
        formatted_names = f"{k.capitalize()} {v.capitalize()}"
        full_name.append(formatted_names)

    return full_name


persons ={
    "jean":"valijean",
    "grace":"hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}    

print(array_of_names(persons))