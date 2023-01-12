#print(bool(0))
#print(bool(1))
#print(bool(1123.23))
#print(bool(-500))

#----------------------------------------

#print(bool(None))
#print(bool('asidad'))
#print(bool(' '))
#print(bool('What do you call a pig doing karate? Pork Chop!'))

#----------------------------------------

#list = []
#print(bool(list))
#list = ['l', 'i', 's', 't']
#print(bool(list))

#----------------------------------------

#year = input('Year of birth: ')

#if not bool(year.rstrip()):
#    print('You need to enter a value for your year of birth.')

#----------------------------------------

#print(dir(['a', 'short', 'list']))

#----------------------------------------

#popcorn = 'I love popcorn!'
#print(dir(popcorn))
#help(popcorn.upper)
#print(popcorn.upper())

#----------------------------------------

#print(eval('10*5'))
#print(eval('''if True:
#                print('this won't work at all!'''))

#----------------------------------------

#calc = input('Enter a calculation: ')
#print(eval(calc))

#----------------------------------------

smalltext = '''print('This')
print('is')'''

exec(smalltext)