import re

string1 = input(f'Enter an irregular string: ')

def regular_string(string):
    result_string = ' '.join(filter(None,string.split(' ')))
    return result_string


print(regular_string(string1))