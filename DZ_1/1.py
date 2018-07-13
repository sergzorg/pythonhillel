#!/usr/bin/python3
##by Sergey Zhukanov

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def gen_sqr_dict(keys):
    sqr_table={}
    for x in keys:
        sqr_table[x]=pow(x,2)
    return(sqr_table)

sqr_dict = gen_sqr_dict(keys)
print(sqr_dict)
