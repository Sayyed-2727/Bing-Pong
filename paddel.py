from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_len=1, stretch_wid=5)
        
    def go_up(self):
        self.goto(x= self.xcor(), y= self.ycor() + 40)
    def go_down(self):
        self.goto(x= self.xcor(), y= self.ycor() -40)