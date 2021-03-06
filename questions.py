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
        uservar.name = input("What is your name: ")
        answer = input("%s...is that correct?" % uservar.name)
        if answer.lower() in responses.yes:
            iq2()
        if answer.lower() in responses.no:
            continue

def iq2():
    while True:
        answer = input("Ok {}, would you like to play on Easy, Medium, or Hard? " .format(uservar.name))
        if answer.lower() in responses.easy:
            scorekeeper.money = 100000
            scorekeeper.age = 18
            scorekeeper.slife = 100
            iq3()
        if answer.lower() in responses.medium:
            scorekeeper.money = 75000
            scorekeeper.age = 21
            scorekeeper.slife = 75
            iq3()
        if answer.lower() in responses.hard:
            scorekeeper.money = 65000
            scorekeeper.age = 25
            scorekeeper.slife = 50
            iq3()
        else:
            print("invalid input")
            continue

def iq3():
    while True:
        answer = input("{} have you played before? ".format(uservar.name))
        if answer.lower() in responses.yes:
            while True:
                answer1 = input("Would you like to review the rules and commands? ")
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
        answer = input("Ok...Ready to begin? ")
        if answer.lower() in responses.yes:
            iq5()
        if answer.lower() in responses.no:
            print("Ok...going back to main menu")
            time.sleep(1)
            iq1()


def iq5():
    while True:
        answer = input("Your the first step in your career is getting your pilots license. Do you want to get it "
                       "through a college program or a local flight school? ")
        if answer.lower() in responses.college:
            print("Alright! Pack your beer bong, we're going to college! ")
            jobs.college()

        if answer.lower() in responses.local:
            print("Hopefully a smart choice...Move into your parents basement and keep that sweet job at Applebee's "
                  "while you pay your way through flight school. ")
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
        answer = input("Which college do you want to go to? (Embry-Riddle, Purdue, University of North Dakota,"
                       " Utah Valley University) ")
        if answer.lower() in responses.riddle:
            scorekeeper.change_money(-10000)
            scorekeeper.change_slife(-50)
            scorekeeper.change_interview(10)
            college = answer.lower()
            print("Welcome to the Harvard of the Skies...hopefully this won't taint your career...")
            cq2()

        if answer.lower() in responses.dakota:
            scorekeeper.change_slife(10)
            scorekeeper.change_interview(5)
            college = answer.lower()
            print("Welcome to The University of North Dakota")
            cq2()

        if answer.lower() in responses.uva:
            scorekeeper.change_money(10000)
            scorekeeper.change_slife(-10)
            college = answer.lower()
            print("Welcome to Utah Valley!")
            cq2()

        if answer.lower() in responses.purdue:
            scorekeeper.change_interview(5)
            scorekeeper.change_slife(15)
            scorekeeper.change_money(-1000)
            college = answer.lower()
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
                                     " what do you say...risk the DUI? "))
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
    scorekeeper.change_age(1)
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
    scorekeeper.change_age(1)
    if college in responses.riddle:
        while True:
            answer = input(textwrap.fill("Spring Break is fast approaching. Do you want to rent a plane and go to the"
                                         "keys? (You'll build get some experience, but for a cost..."))
            if answer.lower() in responses.yes:
                scorekeeper.dice(50)
                while not scorekeeper.outcome:
                    scorekeeper.change_interview(5)
                    scorekeeper.change_slife(-10)
                    scorekeeper.change_money(-500)
                    print(textwrap.fill("Well...unfortunately, the plane lost a fuel pump and you spent your spring "
                                        "break in everglade city. Good thing you're still alive though, now you can "
                                        "use this for a TMAT in future interviews! "))
                    scorekeeper.masterpull()
                    cq5()
                while scorekeeper.outcome:
                    scorekeeper.change_slife(10)
                    scorekeeper.change_money(-1000)
                    print("Your trip was pretty uneventful. I guess that's good!")
                    scorekeeper.masterpull()
                    cq5()
            if answer.lower() in responses.no:
                scorekeeper.change_slife(-5)
                print(textwrap.fill("Everyone else left for spring break...including the flight school dispatcher. "
                                    "You literally did nothing all week."))
                scorekeeper.masterpull()
            else:
                print("Invalid option")
                continue
    if college in responses.purdue:
        while True:
            answer = input(textwrap.fill("A classmate wants to know if you will fly them home for the weekend in "
                                         "return for some spending money...Do you want to take them?"))
            if answer.lower() in responses.yes:
                scorekeeper.dice(50)
                while not scorekeeper.outcome:
                    scorekeeper.change_interview(5)
                    scorekeeper.change_money(500)
                    print(textwrap.fill("While enroute, your friend got really sick. You diverted to Indianapolis. "
                                        "It was your first emergency. Save that for future interview experience!"))
                    scorekeeper.masterpull()
                    cq5()
                while scorekeeper.outcome:
                    scorekeeper.change_slife(-10)
                    scorekeeper.change_money(500)
                    print(textwrap.fill("That was pretty uneventful. You ended up just spending the weekend with your"
                                        " friend and his weird distant relatives"))
                    scorekeeper.masterpull()
                    cq5()
            if answer.lower() in responses.no:
                scorekeeper.change_slife(5)
                scorekeeper.change_money(-100)
                print("You stayed in Lafayette for the weekend and went to the bars instead...")
                scorekeeper.masterpull()
                cq5()
            else:
                print("Invalid option")
                continue
    if college in responses.uva:
        while True:
            answer = input(textwrap.fill("You decide the weather is nice enough for some aerial sight seeing..."
                                         "do you want to rent the cheapest airplane you can find?"))
            if answer.lower() in responses.yes:
                scorekeeper.dice(50)
                while not scorekeeper.outcome:
                    scorekeeper.change_interview(5)
                    scorekeeper.change_money(-500)
                    print(textwrap.fill("Your questionable plane suffered engine failure while somewhere over the "
                                        "salt flats. Luckily you lived. This experience should come in handy for "
                                        "future interviews"))
                    scorekeeper.masterpull()
                    cq5()
                while scorekeeper.outcome:
                    scorekeeper.change_money(-500)
                    print("You got some nice pictures of the Great Salt Lake...isn't that nice?")
                    scorekeeper.masterpull()
                    cq5()
            if answer.lower() in responses.no:
                scorekeeper.change_slife(10)
                print(textwrap.fill("You decided to just slum it around campus...then you found a party! "
                                    "You begrudgingly attend and found some people who aren't mormon@ "))
                scorekeeper.masterpull()
                cq5()
            else:
                print("Invalid option")
                continue
    if college in responses.dakota:
        while True:
            answer = input(textwrap.fill("A local farmer wants you to fly over his land and help him find a missing "
                                         "cow. He said he'd pay you in steak. You interested?"))
            if answer.lower() in responses.yes:
                scorekeeper.dice(50)
                while not scorekeeper.outcome:
                    scorekeeper.change_interview(5)
                    scorekeeper.change_money(-100)
                    print(textwrap.fill("The weather turned bad unexpectedly and you were forced to land in the "
                                        "farmers field. Luckily nobody was hurt and you got a sweet interview "
                                        "story..."))
                    scorekeeper.masterpull()
                    cq5()
                while scorekeeper.outcome:
                    scorekeeper.change_money(-100)
                    print(textwrap.fill("That went pretty well...You got a free steak too"))
                    scorekeeper.masterpull()
                    cq5()
            if answer.lower() in responses.no():
                scorekeeper.change_slife(-5)
                scorekeeper.change_interview(5)
                print(textwrap.fill("You spent the weekend stuffing your face with cheese curds instead...No shame"))
                scorekeeper.masterpull()
                cq5()

            else:
                print("Invalid option")
                continue


def cq5():
    sys.exit()