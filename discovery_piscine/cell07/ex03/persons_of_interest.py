#!/usr/bin/env python3
"""  persons_of_interest.py """
def famous_births(scientists):
    """ famous_births """
    result = sorted(scientists.items(), key=lambda item: int(item[1]['date_of_birth']))
    #result = [f'{} {} for k, v in res']
    result = [name[1] for name in result]
    for i in result:
        print(f'{list(i.values())[0]} is a great scientist born in {list(i.values())[1]}.')

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
