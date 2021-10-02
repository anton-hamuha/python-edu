num = input('enter an integer:')
def square(num):
    if not num.isdigit():
        return 'invalid entry'
    num = int(num)
    return num * num
print(num, 'squared is:', square(num))
