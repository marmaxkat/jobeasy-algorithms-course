a = int(input('Input vallue a:  '))
b = int(input('Input vallue b:  '))


print(f'a = {a}, b = {b}')


# option 1
tenp = a
a = b
b = tenp

print(f'a = {a}, b = {b}')

# option 2
a = a + b
b = a - b
a = a - b

print(f'a = {a}, b = {b}')

# option 3
a , b = b, a
print(f'a = {a}, b = {b}')


string= 'Hello world'[::-1]
print(string)