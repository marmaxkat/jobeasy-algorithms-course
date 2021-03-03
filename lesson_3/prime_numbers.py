def is_prime(given_num):
    if given_num < 2:
        return False
    for number in range(2, given_num):
        if given_num % number == 0:
            return False
    return True

print(is_prime(2))


def prime_numbers(num):
    result = []
    for number in range(2, num):
        if is_prime(number):
            result.append(number)
    return result


print((prime_numbers(100)))