import scorekeeper
import uservar
import responses
import jobs
import time
import sys
import textwrap

college = uservar.college
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
        scorekeeper.age = 18
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
    global college
    while True:
        answer = input("Which college do you want to go to? (Embry-Riddle, Purdue, University of North Dakota"
                       "Utah Valley University")
        if answer.lower() in responses.riddle:
            scorekeeper.change_money(-10000)
            scorekeeper.change_slife(-50)
            scorekeeper.change_interview(10)
            college = responses.riddle
            print("Welcome to the Harvard of the Skies...hopefully this won't taint your career...")
            cq2()

        if answer.lower() in responses.dakota:
            scorekeeper.change_slife(10)
            scorekeeper.change_interview(5)
            college = responses.dakota
            print("Welcome to The University of North Dakota")
            cq2()

        if answer.lower() in responses.uva:
            scorekeeper.change_money(10000)
            scorekeeper.change_slife(-10)
            college = responses.uva
            print("Welcome to Utah Valley!")
            cq2()

        if answer.lower() in responses.purdue:
            scorekeeper.change_interview(5)
            scorekeeper.change_slife(15)
            scorekeeper.change_money(-1000)
            college = responses.purdue
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
                scorekeeper.change_money(-8000)
                scorekeeper.change_interview(-50)
                scorekeeper.masterpull()
                cq3()

            while scorekeeper.outcome:
                print("Hey! Congrats on not getting a DUI. That was pretty stupid of you. At least you get some reward"
                      "for your stupidity. You're now a full member of Alpha Sigma Sigma!")
                scorekeeper.change_interview(30)
                scorekeeper.masterpull()
                cq3()
        if answer.lower() in responses.no:
            print("Well...you made a smart choice. Your frat brothers hazed the crap out of you before kicking you out"
                  "of the house, but at least you didn't ruin your future.")
            scorekeeper.masterpull()
            cq3()
        else:
            print("Invalid option")
            continue


def cq3():
    if college in responses.riddle:
        while True:
            answer = input(textwrap.fill("You met the only girl in Daytona dumb enough to date someone from riddle!"
                                         " Do you want to try and take her on a date?"))
            if answer.lower() in responses.yes:
                scorekeeper.dice(10)
                while not scorekeeper.outcome:
                    scorekeeper.change_slife(-10)
                    print("Wow....just wow....that ended horribly. You're probably going to be single for life")
                    scorekeeper.masterpull()
                    cq4()
                while scorekeeper.outcome:
                    scorekeeper.change_slife(10)
                    scorekeeper.change_money(-1000)
                    print("Hey...somehow you mananged to get a second date. Airplane rentals are costly though...")
                    scorekeeper.masterpull()
                    cq4()
            if answer.lower() in responses.no:
                scorekeeper.change_slife(-15)
                scorekeeper.change_interview(5)
                print("You probably saved yourself public humilation. Way to spend that energy learning airport"
                      " codes though!")
                scorekeeper.masterpull()
                cq4()
            else:
                print("Invalid option")
                continue
    if college in responses.purdue:
        while True:
            answer = input(textwrap.fill("Its homecoming in Layfatte! Are you going to go hard as fuck "
                                         "this weekend?"))
            if answer.lower() in responses.yes:
                scorekeeper.dice(75)
                while not scorekeeper.outcome:
                    scorekeeper.change_slife(15)
                    scorekeeper.change_money(-1000)
                    print("Wow! What a weekend...not 100% sure what happened. But you woke up in a"
                          " weird apartment in a monkey outfit. Wonder how much you spent on fireball?")
                    scorekeeper.masterpull()
                    cq4()
                while scorekeeper.outcome:
                    scorekeeper.change_slife(-10)
                    scorekeeper.change_money(-500)
                    print(textwrap.fill("Not sure what happened...but you lost your keys, phone, and wallet. "
                                        "Also you embarrased yourself in front of that cute little asian girl "
                                        "from chem 204"))
                    scorekeeper.masterpull()
                    cq4()
            if answer.lower() in responses.no:
                scorekeeper.change_slife(-15)
                scorekeeper.change_interview(5)
                print("Woah there party monster...save some of the studying for a school night...")
                scorekeeper.masterpull()
                cq4()
            else:
                print("Invalid option")
                continue
    if college in responses.uva:
        while True:
            answer = input(textwrap.fill("The mormon tabernacle choir is hosting a lock in this weekend for the"
                                         "youth community. You in for a crazy weekend?"))
            if answer.lower() in responses.yes:
                scorekeeper.dice(25)
                while not scorekeeper.outcome:
                    scorekeeper.change_slife(-5)
                    print("You had a blast with your invisible friend")
                    scorekeeper.masterpull()
                    cq4()
                while scorekeeper.outcome:
                    scorekeeper.change_slife(5)
                    print("Look...other people also showed up. You made a friend!")
                    scorekeeper.masterpull()
                    cq4()
            if answer.lower() in responses.no:
                scorekeeper.change_slife(5)
                print("You went against the social norms in Utah...just like a normal college student!")
                scorekeeper.masterpull()
                cq4()
            else:
                print("Invalid option")
                continue
    if college in responses.dakota:
        while True:
            answer = input(textwrap.fill("The boys are going out to get rowdy in bismark...You in?"))
            if answer.lower() in responses.yes:
                scorekeeper.dice(75)
                while not scorekeeper.outcome:
                    scorekeeper.change_slife(15)
                    scorekeeper.change_money(-500)
                    print("You had a good time! No felony charges or accidental deaths...just a massive bar tab")
                    scorekeeper.masterpull()
                    cq4()
                while scorekeeper.outcome:
                    scorekeeper.change_slife(-10)
                    scorekeeper.change_money(-500)
                    print(textwrap.fill("yeah...you couldn't quite keep up. You ended up passing out on the "
                                        "sidewalk and got a public intoxication ticket. Bummer"))
                    scorekeeper.masterpull()
                    cq4()
            if answer.lower() in responses.no():
                scorekeeper.change_slife(-5)
                scorekeeper.change_interview(5)
                print("Well, maybe your friends will invite you out again. Or they'll just find someone "
                      "who is actually fun. You sure did study alot though")
                scorekeeper.masterpull()
                cq4()

            else:
                print("Invalid option")
                continue


def cq4():
    sys.exit()

