#!/usr/bin/python3
##by Sergey Zhukanov
import random

def modify_list(s):
    vowels = [ 'A', 'E', 'I', 'O', 'Q', 'Y' ]
    consonants = [ 'B', 'C', 'D', 'F', 'G', 'H', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    phrase = list(s)
    for x in range(len(phrase)):
        if phrase[x] in consonants:
            phrase[x] = vowels[random.randrange(len(vowels))]
    result = ''.join(phrase)
    return(result)

in_string = input('Enter your string in UPPER case: ')
print(modify_list(in_string))
