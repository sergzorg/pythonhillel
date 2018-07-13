#!/usr/bin/python3
##by Sergey Zhukanov

dict_one = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
dict_two = { 'a': 6, 'b': 7, 'z': 20, 'x': 40 }
print(set(dict_one.keys()).intersection(set(dict_two.keys())))
