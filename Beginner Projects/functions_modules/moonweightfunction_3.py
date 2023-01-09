import sys
#----------------------------------------------------------
#years = 15
#weight = 120
#----------------------------------------------------------

def moon_weight():
    print('What is your weight?')
    weight = int(sys.stdin.readline())
    print('How much weight do you gain every year?')
    inc = float(sys.stdin.readline())
    print('How many years would you like to run the simulation for?')
    years = int(sys.stdin.readline())
    cal = weight
    for x in range(years):
        cal += inc
        print('Year: %s, Weight: %s' % (x, cal))

moon_weight()
