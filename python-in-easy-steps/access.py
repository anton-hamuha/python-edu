file = open('example.txt', 'w')
print('file name:', file.name)
print('file open mode:', file.mode)
print('readable:', file.readable())
print('writable:', file.writable())
def get_status(f):
    if(f.closed != false):
        return 'closed'
    else:
        return 'open'
print('file status:', get_status(file))
file.close()
print('\nfile status:', get_status(file))