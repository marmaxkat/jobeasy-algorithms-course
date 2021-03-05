from math import floor
from math import ceil


def split_in_half(string):
    strind_len = len(string)
    print(strind_len)
    half = ceil(strind_len // 2)
    print(half)
    left = string[:half]
    right = string[half:]
    print(left)
    print(right)
    return  right + left



print((split_in_half('bbbbbcaaaaa')))