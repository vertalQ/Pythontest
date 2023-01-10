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
    def __init__(self, spots, friend):
        self.giraffe_spots = spots
        self.friend = friend
    def left_foot_forward(self):
        print('left foot forward')
    def left_foot_backward(self):
        print('left food backward')
    def right_foot_forward(self):
        print('right foot forward')
    def right_foot_backward(self):
        print('right food backward')
    def dance(self):
        self.left_foot_backward()
        self.left_foot_forward()
        self.right_foot_backward()
        self.right_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()
    def sing(self):
        print('La la la!')


dancingGiraffe = Giraffes(100, 'Unknown')
dancingGiraffe.dance()

#class count:
#    def add(self):
#        count += 1
#    def yell(self):
#        print(count)
#--------------------------------

#reginald = Giraffes()
#harold = Giraffes()
#ozwald = Giraffes(100, 'Gertrude')
#gertude = Giraffes(1020, 'Ozwald')
#print(ozwald.giraffe_spots, ozwald.friend)
#print('...')
#print(gertude.giraffe_spots, gertude.friend)

