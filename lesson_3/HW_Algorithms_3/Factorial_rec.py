n = int(input('Input number: '))

def factorial_rec(number):
    if number < 0:
        return 'I don\'t like to work with Gamma Function'
    else:
        return 1 if (number == 0 or number == 1) else number * factorial_rec(number - 1)

print(factorial_rec(n))