import scorekeeper
import responses

# game specific information

def difficulty():
    while scorekeeper.money == 0:
        level = input("Select your difficulty (easy, medium, hard)")

        if level.lower() == "easy":
            scorekeeper.money = 100000
            break

        if level.lower() == "medium":
            scorekeeper.money = 75000
            break

        if level.lower() == 'hard':
            scorekeeper.money = 50000
            break

        else:
            print("sorry, I didn't quite get that")
            continue

    print("Ok, your starting capital will be {}" .format(scorekeeper.money))





# User specific information

name = 0

def getname():
    global name
    name = input("What is your name?")



