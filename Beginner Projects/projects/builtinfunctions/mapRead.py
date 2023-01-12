favFruitmap = {'Jason' : 'Apples',
'Arthur' : 'Grapes',
'Amy' : 'Bananas'}
fruit = ['apple', 'banana', 'clementime', 'dragon fruit']
length = len(fruit)
#---------------------------------------------
#for i in range(length):
    #print('The fruit in index %s is %s' % (i, fruit[i])) 
#print(len(favFruitmap))
#---------------------------------------------
numbers = [5, 4, 10, 30, 22]
#print(max(numbers))
letters = 's,t,r,i,n,g,S,T,R,I,N,G'
#print(max(letters))

print(min(numbers))
print(min(letters))
#---------------------------------------------
guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max (player_guesses) > guess_this_number:
    print('Boom! You all lose.')
else:
    print('You win.')