known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']
print(len(known_users))

while True:
    print("hi my name is Travis!")
    name = input("What is your name:").strip()

    if name in known_users:
        print("hello {}!". format(name))
        remove = input("would you like to be removed from the system (y/n)?: ").lower()

        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)

    else:
        print("name not recognised")