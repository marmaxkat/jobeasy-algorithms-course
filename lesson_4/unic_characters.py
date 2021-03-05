def unic_characters(string):
    # result = ''
    # # option 1
    # for char in string:
    #     if result.count(char) == 0:
    #         result += char
    # # option 2
    # for char in string:
    #     if char not in result:
    #         result += char
    # option 3
    return ''.join(set(string))
    # return result

print(unic_characters('asafasafret'))