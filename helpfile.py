import Uservar
import textwrap


def mission():
    print(textwrap.fill("Welcome to your new pilot career. Before we begin lets go over the basic overview of the game."
                        " The goal of {} is to complete your career with the most money and most social life points as "
                        "possible. Keep an eye on your age though! Once you hit 65 the game is over. Your first few "
                        "decisions will be critical to the success of your career. Do your best to not run out of money"
                        " or die, as those will both end in game over."
                        " Now...lets go over some basic commands. ", 70) .format(Uservar.gamename))


def commands():
    print("Answer the questions using whatever makes sense")
    # list of user commands that can be accessed at every question using a term like "commands" or "help"
