from bird import*
zola = bird('beep, beep')
print('\nbuilt-in instance attributes...')
for attrib in dir(zola):
    if attrib[0] == '_':
        print(attrib)
        print('\nclass dictoinary...')
        for item in bird._dict_:
            print(item, ':', bird._dict_[item])
            print('\ninstance dictoinary...')
            for item in zola._dict_:
                print(item, ':', zola._dict_[item])
