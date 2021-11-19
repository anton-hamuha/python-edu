def ifDuplicate(array):
    my_set = set(array)
    if len(array) == len(my_set):
        return 'No duplicates'
    else:
        return 'Contains duplicate'


print(ifDuplicate([1,2,3,4,5]))
print(ifDuplicate([1,2,3,4,5,5]))



