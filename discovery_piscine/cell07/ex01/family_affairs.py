#!/usr/bin/env python3
""" family_affairs.py """
def find_the_redheads(person):
    """ find_the_redheads """
    #lst = [k for k, v in family.items() if v == 'red']
    #return lstvalues
    return list(dict(filter(lambda x: x[1] == 'red', person.items())).keys())

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
