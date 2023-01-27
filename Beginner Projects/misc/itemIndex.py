itemDict = {
'000' : 'air',
'001' : 'apple',
'002' : 'pear',
'003' : 'low level sword',
'004' : 'dragon flesh',
'005' : 'cooked dragon meat'
}

class Item:
    def __init__ (self):
        self.index = 000

i = Item()

def createItem():
    global itemDict
    while int(i.index) <= int(max(itemDict.keys())):
        print('You are current on item %s' % (itemDict[str(i.index)]))
        i.index += 1

createItem()
