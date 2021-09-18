basket = ['apple', 'bun', 'cola']
crate = ['egg', 'fig', 'grape']
print('basket list:', basket)
print('basket elements:', len(basket))
basket.append('damson')
print('appended:', basket)
print('last item removed:', basket.pop())
print('basket list:', basket)
basket.extend(crate)
print('extended:', basket)
del basket[1]
print('item removed:', basket)
del basket[1:3]
print('slice removed:', basket)