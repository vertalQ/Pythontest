years = 15
weight = 120
#----------------------------------------------------------

def moon_weight(weight, inc, years):
    cal = weight
    for x in range(years):
        cal += inc
        print('Year: %s, Weight: %s' % (x, cal))

moon_weight(30, 0.25, 5)
