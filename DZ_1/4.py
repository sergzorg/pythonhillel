#!/usr/bin/python3
##by Sergey Zhukanov
mas = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

def find_min_index(mas):
    sort = sorted(set(mas))
    for x in range(len(mas)):
        if mas[x] == sort[0]:
            min_index = x
    return min_index 

def reverse_massive(mas):
    reverse = []
    for x in range(len(mas)):
        reverse.append(mas[(len(mas)-1-x)])
    return reverse 

print("task 4    :  Input massive  ",mas)
print("task 4.1  :  ",set(mas),"  only unique elements")
print('task 4.2  :  ',sorted(set(mas))[-3:],"  three unique maximal numbers")
print("task 4.3  :  ",find_min_index(mas),"  index of minimal element")
print("task 4.4 v1(my function) :  ",reverse_massive(mas),"  input massive in reverse order")
print("task 4.4 v2(slice)       :  ",mas[::-1],"  input massive in reverse order")
mas.reverse()
print("task 4.4 v3(.reverse)    :  ",mas,"  input massive in reverse order")
