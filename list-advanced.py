foods = ["burgers", "pizza", "pickles", "hot dogs"]

num = int(input("Type in a random number between 0 and 3 - "))

while num in range(4):
    print(foods[num])
    while num not in range(4):
        print("Try again")
        num = int(input("Type in a random number between 0 and 3 - "))
