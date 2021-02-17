year = int(input("Enter Year: "))

# Leap Year Check

def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 400 ==0:
        return True
    else:
        return False


print(is_leap_year(year))
