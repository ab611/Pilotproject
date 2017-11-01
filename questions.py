import scorekeeper
import responses

def qtest():
    while True:
        option = input("yes or no")
        if option == responses.yes:
            scorekeeper.change_money(-10000)
            break
        if option == responses.no:
            scorekeeper.change_money(15000)
            break
        if option == responses.stats:
            scorekeeper.masterpull()
            continue

        else:
            print("invalid option")
            continue

