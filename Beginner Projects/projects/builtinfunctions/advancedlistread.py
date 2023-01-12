creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon', 'troll']
emp_list = []
singular_item = ['Apple']

def readLIST(list):
    leng = len(list)
    if leng <= 0:
        print('There are no items on this list.')
    elif leng == 1:
        print('There is 1 item on this list.')
    elif leng > 1:
        print('There are %s items on this list.' % leng)

readLIST(creature_list)
readLIST(emp_list)
readLIST(singular_item)