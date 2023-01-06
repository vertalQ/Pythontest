import time
t = time
#--------------------------
found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
silly_list = ['one', 'apple', 'orange', 'peel']
count = 0
countGoal = 25
#---------------------------

#for week in range(1, 53):
#    coins = coins + magic_coins - stolen_coins
#    print('Week %s = %s coins' % (week, coins))
#print(found_coins)
#
#if found_coins == 20:
#    print("Untouched and safe.")
#else:
#   print("Value has been modified.")

#for i in silly_list:
#    print('%s is the %s item on the list' % (i, silly_list.index(i)))

#while count != countGoal:
#    time.sleep(0.5)
#    count += 1
#    print(count)
#t.sleep(0.5)
#print('hi')

step = 0
tired = False
badweather = False

while step < 10000:
    print(step)
    if tired == True:
        break
    elif badweather == True:
        break
    else:
        step += 1

