import uservar
import random
import time

money = 0
age = 18
slife = 100
college = 0
outcome = False

def masterpull():
    time.sleep(1)
    print()
    print("Ok {}, here are your updated stats..." .format(uservar.name))
    print("Money:", money)
    print("Age:", age)
    print("Social Life:", slife)
    time.sleep(1)
    print()
    input("Press any key to continue...")
    return

# score change processes
def change(item,num):
    global college
    global money
    global age
    global slife
    item += num

def change_college():
    global college
    college = 1

def change_money(num):
    global money
    money += num


def change_age(num):
    global age
    age += num


def change_slife(num):
    global slife
    slife += num


# interview probability: for regional interview flighthours need to = 1500 (or 1000 if you went to college) and
# interview points above x; LCC interview points above Y; Major interview points above Z for randomization process


interview = 0
flighthours = 0

x = 0
def change_interview(num):
    global interview
    global college
    interview += num
    #Here I will use x from comment above as minimum interview points needed for interview. Then I will also embed flight hours in the equation
    if interview >= x and (flighthours >= 1500 or (flighthours >=1000 and college == 1)):
        print("placeholder")
     # what happens if theyget interview?


def change_flighthours(num):
    global flighthours
    flighthours += num


def dice(num):
    global outcome
    x = int(num)
    y = random.randint(1, 100)
    if x <= y:
        outcome = False
    else:
        outcome = True


