number = int(input('Input first number: '))

def to_bin(number):
    result = ''
    while number > 0:
        # result += str(number % 2)
        # number //= 2
        number, reminder = divmod(number, 2)
        result += str(reminder)
    print(result[::-1])
    return result[::-1]


# print(to_bin(529))
# print(bin(529))


def binary_gap(bin_number):
    max_gap = 0
    counter = 0
    for item in str(bin_number):
        if item == '0':
            counter += 1
        elif item == '1':
            if counter > 0 and counter > max_gap:
                max_gap = counter
            counter = 0
    return max_gap

print(binary_gap(to_bin(number)))

