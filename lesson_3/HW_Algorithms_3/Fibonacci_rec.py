def fibonacci_rec(number):
    if number < 0:
        return 'Not a valid value'
    elif number == 1 or number == 2:
        return 1
    else:
        return fibonacci_rec(number-1) + fibonacci_rec(number-2)


print(fibonacci_rec(10))