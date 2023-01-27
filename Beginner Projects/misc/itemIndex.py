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
    while int(i.index) <= int(max(itemDict.keys())):
        print('You are current on item %s' % (itemDict[str(i.index)]))
        i.index += 1

createItem()
