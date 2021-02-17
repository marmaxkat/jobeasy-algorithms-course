num1 = int(input('Input first number: '))
num2 = int(input('Input second number: '))
num3 = int(input('Input third number: '))


def max_number(n1, n2, n3):
    list_of_numbers = [n1, n2, n3]
    return max(list_of_numbers)


print(f'Largest number: {max_number(num1, num2, num3)}')
