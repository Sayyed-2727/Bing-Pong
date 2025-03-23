from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.rscore = 0
        self.lscore = 0
        self.update_score()
        
    def rpoint(self):
        self.rscore +=1
        self.update_score()
        
    def lpoint(self):
        self.lscore +=1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(100,240)
        self.write(self.rscore, align=("center"), font=("courier",40,"normal"))
        self.goto(-100,240)
        self.write(self.lscore, align= "center", font= ("courier", 40, "normal"))
        