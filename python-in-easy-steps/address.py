from Bird import*
chick = Bird('cheep, cheep!')
chick.age = '1 week'
print('\nchick says:', chick.talk())
print('chick age:', chick.age)
chick.age = '2 weeks'
print('chick now:', chick.age)
setattr(chick, 'age', '3 weeks')
print('\nchick attributes...')
for attrib in dir(chick):
    if attrib[0] != '_':
        print(attrib, ':', getattr(chick, 'age'))
        delattr(chick, 'age')
        print('\nchick age attribute?', hasattr(chick, 'age'))
