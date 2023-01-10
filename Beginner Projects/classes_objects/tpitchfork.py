import turtle

class Lines:
    def __init__(self):
        self.t = turtle.Pen()
        self.base = 50
        self.side1 = 20
        self.side2 = 30
    def line1div1(self):
        self.t.forward(self.base)
        self.t.left(90)
        self.t.forward(self.side1)
        self.t.right(90)
        self.t.forward(self.side1)
    def line1div2(self):
        self.t.forward(self.base)
        self.t.right(90)
        self.t.forward(self.side1)
        self.t.left(90)
        self.t.forward(self.side1)

r = Lines()
r.line1div1
r.line1div2

#---------------------------
turtle.mainloop()