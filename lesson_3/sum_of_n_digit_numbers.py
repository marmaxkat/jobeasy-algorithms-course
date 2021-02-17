from random import randint

n = int(input('Imput a number of digits: '))
first_num = pow(10, n-1)
last_num = pow(10, n) - 1

random_number = randint(first_num, last_num)
print(f'random number: {random_number}')


def sum_of_n(number, n):
    temp_num = 0
    while n > 0:
        temp_num += number % 10
        number = number // 10
        n -= 1
    return temp_num


print(sum_of_n(random_number, n))
