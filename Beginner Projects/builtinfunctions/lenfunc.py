def name():
    while True:
        nameInp = input('Enter your name. Cannot be more than 12 characters!: ')
        if len(nameInp) > 12:
            print('Name is greater than 12 characters! Try again.')
        else:
            print('Name allowed!')
            break

name()