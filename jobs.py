import questions
import scorekeeper
import responses
import uservar

# education fork
def college():
    # As soon as this choice is selected, the following "scores" are updated
    scorekeeper.change_interview(10)
    scorekeeper.change_money(-50000)
    scorekeeper.change_age(4)
    scorekeeper.change_slife(10)
    scorekeeper.change_flighthours(200)


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


def skywest():


def republic():


def piedmont():


def corperate():

# LCC fork
def spirit ():


def jetblue():


# major airline fork
def southwest():


def united():


def american():


def delta():