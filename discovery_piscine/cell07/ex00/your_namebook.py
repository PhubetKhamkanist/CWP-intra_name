#!/usr/bin/env python3
""" your_namebook.py """
def array_of_names(person):
    """ your_namebook.py  """
    return [f'{k.capitalize()} {v.capitalize()}' for k, v in person.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
