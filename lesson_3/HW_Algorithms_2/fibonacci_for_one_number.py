number = int(input('Input first number: '))


def Fibonacci(n):
    if n < 0:
        print('Not a valid value')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(number))