from random import randint

#n = int(input('Imput a number of digits: '))

random_number = randint(100, 999)
print(f'random number: {random_number}')

def sum_of_three(number):
    once = number % 10

    number = number // 10

    tens = number % 10

    hund = number // 10

    return once + tens + hund

print(sum_of_three(random_number))