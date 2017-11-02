import questions
import sys
import scorekeeper
import responses
import uservar

# education fork
def college():
    # As soon as this choice is selected, the following "scores" are updated
    scorekeeper.change_college()
    scorekeeper.change_interview(10)
    scorekeeper.change_money(-50000)
    scorekeeper.change_age(4)
    scorekeeper.change_slife(10)
    scorekeeper.change_flighthours(200)
    questions.cq1()



def pt61():
    # As soon as this choice is selected, the following "scores" are updated
    scorekeeper.change_interview(5)
    scorekeeper.change_money(-25000)
    scorekeeper.change_age(2)
    scorekeeper.change_slife(0)
    scorekeeper.change_flighthours(250)


# time building fork
def fltinst():
    # As soon as this choice is selected, the following "scores" are updated
    scorekeeper.change_interview(5)
    scorekeeper.change_slife(5)
    scorekeeper.change_money(1000)


def survey():
    # As soon as this choice is selected, the following "scores" are updated
    scorekeeper.change_interview(10)
    scorekeeper.change_slife(-75)
    scorekeeper.change_money(10000)



#regional fork
def airwis():
    print("unavailable right now")  # this is just a placeholder...error message thrown off without it
    sys.exit()

def skywest():
    print("unavailable right now")


def republic():
    print("unavailable right now")

def piedmont():
    print("unavailable right now")

def corperate():
    print("unavailable right now")
# LCC fork
def spirit ():
    print("unavailable right now")

def jetblue():
    print("unavailable right now")

# major airline fork
def southwest():
    print("unavailable right now")

def united():
    print("unavailable right now")

def american():
    print("unavailable right now")

def delta():
    print("unavailable right now")
