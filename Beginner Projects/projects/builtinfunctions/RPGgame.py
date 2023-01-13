import time
t = time
#----------------------------------------
coins = 0
#----------------------------------------
class Player:
    def __init__(self):
        self.health = 20
        self.dmg = 2
class Slime:
    def __init__(self):
        self.health = 10
        self.dmg = 2

def beginGame():
    global coins
    while True:
        choice = int(input('''       Choose an Option        
    1. Shop
    2. Go fight slimes.
    Choice: '''))
        if choice == 1:
            print('You are now at the shop.')
        elif choice == 2:
            coins += slimeField()
            break
        else:
            print('''Invalid input. Please pick a choice.
            %s''' % (len('Invalid input. Please pick a choice.') * '='))
            t.sleep(1)

def slimeField():
    print('You are now in the slime field!')
    return 5


beginGame()