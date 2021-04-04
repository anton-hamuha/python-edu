number = input("Random number - ")

print("Your number has " + str(len(number)) + " digits.")  # way 1

count = 0

number = input("Random number - ")

for x in number:  # way 2
    count += 1

print("Your number has {} digits.".format(count))
