n = int(input('Input number: '))


def count_odd_even(num):
    odd_count = 0
    even_count = 0
    while num > 0:
        temp_num = num % 10
        if temp_num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    return even_count, odd_count


even_count, odd_count = count_odd_even(n)
print('even_count: %d' % even_count)
print('odd_count: %d' % odd_count)