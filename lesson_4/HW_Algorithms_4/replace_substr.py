import re

string1 = input(f'Enter a string: ')
substr1 = input(f'Find word: ')
substr2 = input(f'Replace: ')

def replace_substr(string, substr_1, substr_2):
    if substr_1 not in string:
        return f'Can not find {substr_1} in {string}'
    else:
        pattern = re.compile(substr_1, re.IGNORECASE)
        result = pattern.sub(substr_2, string)
    return result


print(replace_substr(string1, substr1, substr2))