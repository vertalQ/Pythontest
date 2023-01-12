favFruitmap = {'Jason' : 'Apples',
'Arthur' : 'Grapes',
'Amy' : 'Bananas'}
fruit = ['apple', 'banana', 'clementime', 'dragon fruit']
length = len(fruit)
#---------------------------------------------
for i in range(length):
    print('The fruit in index %s is %s' % (i, fruit[i]))
    
print(len(favFruitmap))