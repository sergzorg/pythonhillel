#!/usr/bin/python3
##by Sergey Zhukanov

def gen_even_list():
    even_list=[]
    for x in range(100):
        if (x+1) % 2 == 0:
            even_list.append(x+1)
    return(even_list)

print(gen_even_list())
