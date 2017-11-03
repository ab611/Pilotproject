import scorekeeper
import uservar
import responses
import jobs
import time
import sys
import textwrap
# iqX() qustions will be used to the introduction (get username, select difficulty, etc)


def iq1():
    while True:
        uservar.name = input("What is your name")
        answer = input("{}...is that correct?".format(uservar.name))
        if answer.lower() in responses.yes:
            iq2()
        if answer.lower() in responses.no:
            continue

def iq2():
    while True:
        answer = input("Ok {}, would you like to play on Easy, Medium, or Hard?" .format(uservar.name))
        if answer.lower() in responses.easy:
            scorekeeper.money = 100000
            iq3()
        if answer.lower() in responses.medium:
            scorekeeper.money = 75000
            iq3()
        if answer.lower() in responses.hard:
            scorekeeper.money = 50000
            iq3()
        else:
            print("invalid input")
            continue

def iq3():
    while True:
        answer = input("{} have you played before?".format(uservar.name))
        if answer.lower() in responses.yes:
            while True:
                answer1 = input("Would you like to review the rules and commands?")
                if answer1.lower() in responses.yes:
                    print("INSERT HELP FILE HERE")
                    input("Press any key to continue")
                    iq4()
                if answer1.lower() in responses.no:
                    iq4()
                else:
                    print("invalid input")
                    continue
        if answer.lower() in responses.no:
            print("INSERT HELP FILE HERE")
            input("Press any key to continue")
            iq4()
        else:
            print("invalid input")
            continue


def iq4():
    while True:
        answer = input("Ok...Ready to begin?")
        if answer.lower() in responses.yes:
            iq5()
        if answer.lower() in responses.no:
            print("Ok...going back to main menu")
            time.sleep(1)
            iq1()


def iq5():
    while True:
        answer = input("Your the first step in your career is getting your pilots license. Do you want to get it though"
                       "a college program or a local flight school?")
        if answer.lower() in responses.college:
            print("Alright! Pack your beer bong, we're going to college!")
            jobs.college()

        if answer.lower() in responses.local:
            print("Hopefully a smart choice...Move into your parents basement and keep that sweet job at Applebees "
                  "while you pay your way through flight school.")
            jobs.pt61()

        if answer.lower() in responses.stats:
            scorekeeper.masterpull()
            continue

        else:
            print("Invalid option.")
            continue


# cqX() questions will be used for the college flight training path
def cq1():
    while True:
        answer = input("Which college do you want to go to? (Embry-Riddle, Purdue, University of North Dakota"
                       "Utah Valley University")
        if answer.lower() in responses.riddle:
            scorekeeper.change_money(-10000)
            scorekeeper.change_slife(-50)
            scorekeeper.change_interview(10)
            print("Welcome to the Harvard of the Skies...hopefully this won't taint your career...")
            cq2()

        if answer.lower() in responses.dakota:
            scorekeeper.change_slife(10)
            scorekeeper.change_interview(5)
            print("Welcome to The University of North Dakota")
            cq2()

        if answer.lower() in responses.uva:
            scorekeeper.change_money(10000)
            scorekeeper.change_slife(-10)
            print("Welcome to Utah Valley!")
            cq2()

        if answer.lower() in responses.purdue:
            scorekeeper.change_interview(5)
            scorekeeper.change_slife(15)
            scorekeeper.change_money(-1000)
            print("Welcome to Purdue")
            cq2()

        if answer.lower() in responses.stats:
            scorekeeper.masterpull()
            continue

        else:
            print("invalid option. please try again")
            continue

def cq2():
    scorekeeper.change_age(1)
    while True:
        answer = input(textwrap.fill("its rush week! You've had a few drinks when a frat brother calls you and asks to "
                                     "be picked up from the bar. If you say yes, you'll be a shoe in to the fraternity "
                                     "which might help later in your career. If you say no, your greek life is over. So"
                                     " what do you say...risk the DUI?"))
        if answer.lower() in responses.yes:
            scorekeeper.dice(50)
            while not scorekeeper.outcome:
                print("Looks like you got a DUI...Better do some serious resume padding from here on out. Now you have"
                      " to pay those lawyer fees.")
                time.sleep(1)
                scorekeeper.change_money(-8000)
                scorekeeper.change_interview(-50)
                print()
                print(scorekeeper.masterpull())
                time.sleep(2)
                cq3()

            while scorekeeper.outcome:
                print("Hey! Congrats on not getting a DUI. That was pretty stupid of you. At least you get some reward"
                      "for your stupidity. You're now a full member of Alpha Sigma Sigma!")
                scorekeeper.change_interview(30)
                time.sleep(1)
                print()
                print(scorekeeper.masterpull())
                time.sleep(2)
                cq3()
        if answer.lower() in responses.no:
            print("Well...you made a smart choice. Your frat brothers hazed the crap out of you before kicking you out"
                  "of the house, but at least you didn't ruin your future.")
            time.sleep(1)
            print()
            print(scorekeeper.masterpull())
            time.sleep(2)
            cq3()

        else:
            print("Invalid option")
            continue


def cq3():
    sys.exit()
