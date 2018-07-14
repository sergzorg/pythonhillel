#!/usr/bin/python3
##by Sergey Zhukanov

data = [ {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
         {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
         {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
         {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
         {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
         {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

def group_by_city(data):
    cities = []
    sorted_city = {}
    for x in data:
        cities.append(x.get('city', False))
    uniq_cities = set(cities)
    for city in uniq_cities:
        citizens = []
        for dictionary in data:
            if city in dictionary.values():
                dictionary.pop("city")
                citizens.append(dictionary)
        sorted_city[city] = citizens
    return(sorted_city)

print("task 6.1  : sorted by key 'age' \n",sorted(data, key=lambda val: val['age']),"\n")
print("task 6.2  : grouped by key 'city' \n",group_by_city(data),"\n")
