money = 0
age = 18
slife = 100

def masterpull():
    print()
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


# interview probability

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
