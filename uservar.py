import scorekeeper
import responses

# game specific information


def difficulty():
    while scorekeeper.money == 0:
        level = input("Select your difficulty (easy, medium, hard)")

        if level.lower() in responses.easy:
            scorekeeper.money = 100000
            break

        if level.lower() in responses.medium:
            scorekeeper.money = 75000
            break

        if level.lower() in responses.hard:
            scorekeeper.money = 50000
            break

        else:
            print("sorry, I didn't quite get that")
            continue

    print("Ok, your starting capital will be {}" .format(scorekeeper.money))

# ^^^ This will most likely get moved to questions.py, still playing around with format


# User specific information

name = 0
college = 0

def getname():
    global name
    name = input("What is your name?")

# ^^^ This will most likely get moved to questions.py, still playing around with format



