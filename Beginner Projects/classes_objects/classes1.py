count = 0

#--------------------------------
class Things:
    pass
#--------------------------------

class Inanimate(Things):
    pass

class Sidewalks(Inanimate):
    pass

#--------------------------------

class Animate(Things):
    pass

class Animals(Animate):
    def breathe(self):
        print('Breathing')
    def move(self):
        print('Moving')
    def eat_food(self):
        print('Eating')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def sing(self):
        print('La la la!')

#class count:
#    def add(self):
#        count += 1
#    def yell(self):
#        print(count)
#--------------------------------

reginald = Giraffes()
harold = Giraffes()

harold.feed_young_with_milk()
reginald.move()








#count1 = count()
#count2 = count()
#count1.add()
#count1.add()
#count2.add()
#count1.yell()
#count2.yell()