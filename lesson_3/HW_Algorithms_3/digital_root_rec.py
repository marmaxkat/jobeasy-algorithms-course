def digital_root_rec(num):
    if len(str(num)) == 1:
        return num
    sum = 0
    for i in str(num):
        sum += int(i)
    return digital_root_rec(sum)

print(digital_root_rec(5))
print(digital_root_rec(16))
print(digital_root_rec(942))
print(digital_root_rec(132189))
print(digital_root_rec(493193))