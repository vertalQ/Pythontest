years = 15
weight = 120
#----------------------------------------------------------

def moon_weight(weight, inc):
    cal = weight
    for x in range(1, 16):
        cal += inc
        print('Year: %s, Weight: %s' % (x, cal))

moon_weight(30, 0.25)
