def euclid_algoritm(num_1, num_2):
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 = num_1 - num_2
        else:
            num_2 = num_2 - num_1
    return num_1


print((euclid_algoritm(16, 24)))


def euclid_algoritm_pro(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    return num_1 + num_2


print((euclid_algoritm_pro(54, 17)))