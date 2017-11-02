import uservar

money = 0
age = 18
slife = 100

def masterpull():
    print("Ok {}, here are your stats..." .format(uservar.name))
    print("Money:", money)
    print("Age:", age)
    print("Social Life:", slife)
    print()
# score change processes


def change_money(num):
    global money
    x = int(num)
    money = money + x


def change_age(num):
    global age
    x = int(num)
    age = age + x


def change_slife(num):
    global slife
    x = int(num)
    slife = slife + x


# interview probability: for regional interview flighthours need to = 1500 (or 1000 if you went to college) and
# interview points above x; LCC interview points above Y; Major interview points above Z for randomization process


interview = 0
flighthours = 0


def change_interview(num):
    global interview
    x = int(num)
    interview = interview + x


def change_flighthours(num):
    global flighthours
    x = int(num)
    flighthours = flighthours + x
