chars = ['a', 'b', 'c']
fruit = ('apple', 'banana', 'cherry')


print('\nelements:\t', end='')
for item in chars:
    print(item, end='')
print('\nenumerated:\t', end='')
for item in enumerate(chars):
    print(item, end='')