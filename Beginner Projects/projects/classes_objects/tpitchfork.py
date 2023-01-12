import turtle

class Lines:
    def __init__(self):
        self.t = turtle.Pen()
        self.base = 90
        self.sbase = 80
        self.side1 = 30
        self.side2 = 60
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
    def line2div3(self):
        self.t.forward(self.sbase)
        self.t.right(90)
        self.t.forward(self.side2)
        self.t.left(90)
        self.t.forward(self.side2)
    def line2div4(self):
        self.t.forward(self.sbase)
        self.t.left(90)
        self.t.forward(self.side2)
        self.t.right(90)
        self.t.forward(self.side2)

r = Lines()
y = Lines()
ry = Lines()
yr = Lines()
r.line1div1()
y.line1div2()
ry.line2div3()
yr.line2div4()

#---------------------------
turtle.mainloop()