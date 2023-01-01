import time

#age = 19 
##-------------------------------

#if age != 20:
#   print('You are too old!')
#   print('Why are you here?')
#   print('Why aren\'t you mowing a lawn or sorting papers?')


#hair_color = 'brown'
#
#if hair_color == 'brown' or hair_color == 'black':
#    print('Your hair color is %s' % hair_color)
#elif hair_color != 'brown' or 'black':
#    print('Unregistered hair color: %s' % hair_color)

#age = 9
#
#if age >= 10:
#    print('You are too old for jokes!')
#else:
#    print("What\'s brown and sticky? A stick!")

username = 'vertalQ'
password = 'password'


if password == 'password' and username == 'vertalQ':
    print('Access granted.')
elif password != 'password' or username != 'vertalQ':
    print('Access denied.')

age = 10    

while True:
    time.sleep(1)
    if age >= 10 and age <= 13:
        print('What is 13 + 39 + 84 + 155 + 97? A headache!')
    elif age == 21:
        print('You are too old for jokes!')
        break
    else:
        print('Inappropriate age range')
    print(age)
    age += 1