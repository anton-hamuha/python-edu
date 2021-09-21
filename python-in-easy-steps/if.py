num = int(input('please enter a number:'))

if num > 5:
    print('number exceeds 5')
elif num < 5:
    print('number is less than 5')
else:
    print('number is 5')

if num > 7 and num < 9:
    print('number is 8')
if num == 1 or num == 3:
    print('number is 1 or 3')