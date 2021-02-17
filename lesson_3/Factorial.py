import math

n = int(input('Input number: '))

def factorial(number):
    if number < 0:
        return 'I don\'t like to work with Gamma Function'
    if number == 0:
        return 1
    rezult = 1
    for item in range(1, number + 1):
        rezult *= item
    return rezult

print(factorial(n))

