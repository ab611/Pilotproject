import scorekeeper
import responses
import jobs

# iqX() qustions will be used to the introduction (get username, select difficulty, etc)
def iq1():
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
            break

        if answer.lower() in responses.dakota:
            scorekeeper.change_slife(10)
            scorekeeper.change_interview(5)
            print("Welcome to The University of North Dakota")
            break

        if answer.lower() in responses.uva:
            scorekeeper.change_money(10000)
            scorekeeper.change_slife(-10)
            print("Welcome to Utah Valley!")
            break

        if answer.lower() in responses.purdue:
            scorekeeper.change_interview(5)
            scorekeeper.change_slife(15)
            scorekeeper.change_money(-1000)
            print("Welcome to Purdue")
            break

        if answer.lower() in responses.stats:
            scorekeeper.masterpull()
            continue

        else:
            print("invalid option. please try again")
            continue

