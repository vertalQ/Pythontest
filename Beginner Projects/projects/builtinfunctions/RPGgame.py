import time
import sys
t = time
#----------------------------------------
coins = 0
hpPots = 0
#----------------------------------------
class Player:
    def __init__(self):
        self.health = 20
        self.dmg = 2
class Slime:
    def __init__(self):
        self.health = 10
        self.dmg = 2
        
player = Player()

def beginGame():
    global player
    global coins
    global hpPots
    while True:
        choice = int(input('''       Choose an Option        
    1. Shop.
    2. Status.
    3. Go fight slimes.
    4. Heal.
    Choice: '''))
        if choice == 1:
            while True:
                print('You are now at the shop.')
                sCoI = int(input('''Current balance: %s coins
                    1. Purchase a healing potion (2 coins).
                    2. Purchase Greater Sword (10 coins).
                    3. Exit Shop.
                    Choice: ''' % coins))
                if sCoI == 1:
                    if coins >= 2:
                        coins -= 2
                        hpPots += 1
                        print('Purchased potion!')
                        t.sleep(1.5)
                    elif coins < 2:
                        print('Insufficient balance!')
                        t.sleep(1.5)
                elif sCoI == 2:
                    if coins >= 10:
                        coins -= 10
                        player.dmg == 5
                        print('Purchased Great Sword! You now deal 5 damage instead of 2.')
                    t.sleep(1.5)
                elif sCoI == 3:
                    beginGame()
            
        elif choice == 2:
            print('''
                     -------------------
                         Health: %s
                       Purse: %s coins
                     -------------------''' % (player.health, coins))
            t.sleep(3)
        
        elif choice == 3:
            slimeField()
            break
        elif choice == 4:
            if hpPots > 0:
                hpPots -= 1
                player.health == 20
                print('Consumed healing potion! You have %s potion(s) left... ' % hpPots)
                t.sleep(3)
            else:
                print('You have no healing potions to expend!')
                t.sleep(2)
        else:
            print('''Invalid input. Please pick a choice.
            %s''' % (len('Invalid input. Please pick a choice.') * '='))
            t.sleep(1)

def slimeField():
    global player
    global coins
    global hpPots
    print('You are now in the slime field!')
    slime = Slime()
    while True:
        dec = int(input('''You spot a slime, what do you do?
        1. Attack.
        2. Run.
        3. Heal.
        Choice: '''))
        if dec == 1:
            slime.health -= player.dmg
            player.health -= slime.dmg
            print('Slime HP: %s' % slime.health)
            print('Ouch! Player HP: %s' % player.health)
            if player.health <= 0:
                print('You died! Game Over!')
                sys.exit()
            elif slime.health <= 0:
                coins += 3
                print('Slime defeated! Collected 3 coins.')
                choI = input('''Would you like to look for another slime? Y/N
                Choice: ''').lower()
                if choI.strip() == 'y':
                    slimeField()
                elif choI.strip() == 'n':
                    beginGame()
                else:
                    print('Invalid option. Breaking program...')
                    break
        elif dec == 2:
            print('Running away...')
            beginGame()
            break
        elif dec == 3:
            if hpPots > 0:
                hpPots -= 1
                player.health == 20
                print('Consumed healing potion! You have %s potion(s) left... ' % hpPots)
                t.sleep(3)
    


beginGame()