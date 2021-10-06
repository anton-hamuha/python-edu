chars = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
def display(elem):
    assert type(elem)is int, 'argument must be integer!'
    print('list element', elem, '=', chars[elem])
elem = 4
display(elem)
elem = elem/2
display(elem)
