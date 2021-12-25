#improved with user input!

num1 = input("Input number 1 - ")
num2 = input("Input number 2 - ")

def check_nums(x= num1, y= num2):
    if x > y:
        return 'num1 is bigger than num2'
    elif y > x:
        return 'num2 is bigger than num1'
    else:
        return 'both numbers are equal'

print(check_nums())
