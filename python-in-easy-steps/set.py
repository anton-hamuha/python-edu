zoo = ('lion', 'tiger', 'leopard')
print('tuple:', zoo, '\tlength:', len(zoo))
print(type(zoo))

bag = {'red', 'green', 'blue'}
bag.add('yellow')
print('\nset:', bag, '\tlenght', len(bag))
print(type(bag))

print('\nls green in bag set?:', 'green' in bag)
print('is orange in bag set?:', 'orange' in bag)

box = {'red', 'purple', 'yellow'}
print('\nset:', box, '\t\tlength', len(box))
print('common to both sets:', bag.intersection(box))
