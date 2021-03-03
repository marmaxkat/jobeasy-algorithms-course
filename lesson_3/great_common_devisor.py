from lesson_3.divisors import get_divisors


def in_list(num, lisst_of_numbers):
    return num in lisst_of_numbers


def great_common_devisor(num_1, num_2):
    divisors_num_1 = get_divisors(num_1)
    divisors_num_2 = get_divisors(num_2)

    result = []
    for num in divisors_num_1:
        if in_list(num, divisors_num_2):
            result.append(num)
    return max(result)


print(great_common_devisor(24, 16))