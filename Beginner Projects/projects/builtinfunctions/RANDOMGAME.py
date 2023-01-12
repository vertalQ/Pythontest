import random
#------------------------------------------------------
def gameChoice():
    while True:
        choice = int(input('''Pick a game by inputting the number: 
    1. Number Guess.
    2. Fruit Guess.
    3. Less than or Greater.
    4. Quit program.
    Game: '''))
        if choice == 1:
            numberGuess()
            break 
        elif choice == 2:
            print("You are now playing: 'Fruit Guess.'")
        elif choice == 3:
            print("You are now playing: 'Less than or Greater.'")
        elif choice == 4:
            print('Quitting program...')
            break
        else:
            print('Invalid input. Please pick a number from the list.')

def numberGuess():
    print("You are now playing: 'Number Guess.' ")
    while True: 
        gusnum = random.randint(0,20)
        playerGuess = int(input('Correctly guess a number from 0 to 20!: '))
        if int(playerGuess) == gusnum:
            chN = input('Well done! Would you like to play again? Y/N: ').lower()
            if chN == 'n':
                break
            elif chN == 'menu':
                gameChoice()
                break
        else:
            print('Incorrect! Try again!')
        

        


gameChoice()
    