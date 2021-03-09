string1 = input(f'Enter a string: ')
substr1 = input(f'Find: ')


def substr_count(string, substr):
    result = len(string.split(substr)) - 1
    if result == 0:
        return f'{substr} is not in {string}'
    else:
        return result


print(substr_count(string1, substr1))
