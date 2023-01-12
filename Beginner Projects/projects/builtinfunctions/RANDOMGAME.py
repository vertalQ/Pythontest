import random
#------------------------------------------------------
fruits = ['apple', 'banana', 'melon', 'strawberries', 'mango']
score = 0
#------------------------------------------------------
def gameChoice():
    while True:
        choice = int(input('''Pick a game by inputting the number: 
    1. Number Guess.
    2. Fruit Guess.
    3. Less than or Greater.
    4. Quit program.
    5. Check score.
    Game: '''))
        if choice == 1:
            numberGuess()
            break 
        elif choice == 2:
            fruitGuess()
            break
        elif choice == 3:
            greaterOrLess()
            break
        elif choice == 4:
            print('Quitting program...')
            break
        elif choice == 5:
            print('Your score is: %s' % score)
        else:
            print('Invalid input. Please pick a number from the list.')

def numberGuess():
    print("You are now playing: 'Number Guess.' ")
    gusnum = random.randint(0,10)
    while True: 
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

def fruitGuess():
    print("You are now playing: 'Fruit Guess.' ")
    while True: 
        gusfru = random.choice(fruits)
        playerGuess = input('''Correctly guess a fruit from the following list!: 
        %s
        Guess: ''' % fruits)
        if playerGuess == gusfru:
            chN = input('Well done! Would you like to play again? Y/N: ').lower()
            if chN == 'n':
                break
            elif chN == 'menu':
                gameChoice()
                break
        else:
            print('Incorrect! Try again!')

def greaterOrLess():
    print("You are now playing: 'Less than or Greater.'")
    while True:
        com1 = random.randint(0, 100)
        com2 = random.randint(0, 100)
        answer = None
        if com1 > com2:
            answer = 'greater'
        elif com1 < com2:
            answer = 'less'
        elif com1 == com2:
            answer = 'equal' 
        playerInput = input('Is %s greater, less, or equal to %s?: ' % (com1, com2)).lower()
        if playerInput == answer:
            chN = input('Well done! Would you like to play again? Y/N: ').lower()
            if chN == 'n':
                break
            elif chN == 'menu':
                gameChoice()
                break
        else:
            print('Incorrect! Try again!')

gameChoice()
    