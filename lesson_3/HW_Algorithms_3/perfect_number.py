number = int(input('Enter number: '))


def is_perfect(n):
    perfect_sum = 0

    for i in range(1, n):
        if n % i == 0:
            perfect_sum += i

    return perfect_sum == n


if is_perfect(number):
    print('%d is PERFECT' %(number))
else:
    print('%d is NOT PERFECT' %(number))
