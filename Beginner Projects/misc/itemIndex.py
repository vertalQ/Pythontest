itemDict = {
'0' : 'air',
'1' : 'apple',
'2' : 'pear',
'3' : 'low level sword',
'4' : 'dragon flesh',
'5' : 'cooked dragon meat'
}

class Item:
    def __init__ (self):
        self.index = 0

i = Item()

def createItem():
    global itemDict
    global i
    print('You are currently on item %s [INDEX: %s]' % (itemDict[str(i.index)], i.index))
    while True:
        querINP = input('^ or \/ (a/s): ').lower()
        if querINP == 'a':
            if i.index == int(max(itemDict.keys())):
                print('Reached max!')
                #i.index -= 1
            else:
                i.index += 1
                print('You are on item %s [INDEX: %s]' % (itemDict[str(i.index)], i.index))
        elif querINP == 's':
            if i.index == int(min(itemDict.keys())):
                print('Reached min!')
                #i.index += 1
            else:
                i.index -= 1
                print('You are on item %s [INDEX: %s]' % (itemDict[str(i.index)], i.index))
        elif querINP == 'exit':
            return 'Exited program.'

print(createItem())
