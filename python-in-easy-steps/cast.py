a = input('Enter a number:')
b = input('Now enter another number:')
sum = a + b
print('\nData type sum:',sum,type(sum))
sum = int(a) + int(b)
print('Data type sum:',sum,type(sum))
sum = float(sum)
print('Data type sum:',sum,type(sum))
sum = chr( int(sum))
print('Data type sum:',sum,type(sum))