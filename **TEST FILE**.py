# created soley to test different scripts

import uservar
import questions
import scorekeeper
import responses
import jobs

def test():
    while True:
        choice = input("You got an interview, would you like to go?")
        if choice.lower() in responses.yes:
            scorekeeper.dice(50)
            if scorekeeper.outcome == False:
                print("sorry, you didnt get the job")
                break

            if scorekeeper.outcome == True:
                print("Congrats. you got the job")
                jobs.airwis()
                break

        if choice.lower() in responses.no:
            print("Maybe next time...")
            break

        else:
            print("Invalid input")
            continue


questions.iq1()
