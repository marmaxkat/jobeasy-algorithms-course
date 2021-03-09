string1 = input(f'Enter a string: ')

def longest_word(string):
   str_list = string.split()
   sort_list = sorted(str_list, key=len)
   return sort_list[-1]


print(longest_word(string1))
