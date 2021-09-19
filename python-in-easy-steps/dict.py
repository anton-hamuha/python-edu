dict = {'name': 'bob', 'ref': 'python', 'sys': 'win'}
print('dictionary:', dict)

print('\nreference:', dict['ref'])
print('\nkeys:', dict.keys())
del dict['name']
dict['user'] = 'tom'
print('\ndictionary:', dict)
print('\nls there a name key?:', 'name' in dict)
