known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']
print(len(known_users))

while True:
    print("hi my name is Travis!")
    name = input("What is your name:").strip().capitalize()

    if name in known_users:
        print("hello {}!". format(name))
        remove = input("would you like to be removed from the system (y/n)?: ").lower().strip()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("no problem, i didn't want you to leave anyway!")


    else:
        print("hmm i don't think i have met you yet {}".format(name))
        add_me = input("would you like to be added to the system (y/n)?:").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("no worries, see you around!")