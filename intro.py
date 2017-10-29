import questions
import Uservar
import helpfile


def start():
    print("Hello. Welcome to {}. Lets start off by asking a few questions..." .format(Uservar.gamename))
    questions.q1()
    def loop1():
        rules = input("Ok {}, do you need me to explain the rules?" .format(Uservar.username))
        Uservar.pause(2)
        validinput = False
        while not validinput:
            try:
                if rules.lower() in questions.yes:      # This may be able to be simplified, let me know what you think
                    helpfile.mission()
                    print()
                    input("Press Enter to Continue")
                    validinput = True
                    Uservar.pause(4)
                    helpfile.commands()
                    continue

                if rules.lower() in questions.no:
                    print('INSERT NEXT OPTION HERE')    # Need to add option to just pull up command list
                    validinput = True
                    continue

                else:
                    print("Sorry, I didn't understand that.")
                    loop1()
            except:
                print("Sorry, I didn't understand that.")
                loop1()

    loop1()


start()