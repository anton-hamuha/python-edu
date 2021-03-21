import random

fortune = []
fortune.append("YES!")
fortune.append("NO!")
fortune.append("Maybe?")


cont = "Yes"
while cont == "Yes":
    print("Ask me a yes or no question")
    question = input()
    answer = random.choice(fortune)
    print(answer)
    print ("Do you want to ask another question?")
    cont = input("Yes or No: ")