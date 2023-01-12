
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
            print("You are now playing: 'Number Guess.' ")
        elif choice == 2:
            print("You are now playing: 'Fruit Guess.'")
        elif choice == 3:
            print("You are now playing: 'Less than or Greater.'")
        elif choice == 4:
            print('Quitting program...')
            break
        else:
            print('Invalid input. Please pick a number from the list.')

gameChoice()
    