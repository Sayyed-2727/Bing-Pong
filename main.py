from turtle import Screen, Turtle
from paddel import Paddle
from ball import Ball
from score import Score
import time
import winsound

# Screen adjustment
screen = Screen()
screen.title("Ping Pong game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Creating objects
r_paddel = Paddle((350,0))
l_paddel = Paddle((-350,0))
ball = Ball()
score = Score()


# Screen activation
screen.listen()
screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")
screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")

# Ball movement
default_sleep = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(default_sleep)
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)
    
    # ball bounce  [vertical]
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_move *= -1
    
    # ball bounce on paddel [horizontal]
    if (ball.xcor() > 330 and ball.distance(r_paddel) <= 50)  or (ball.xcor() < -330 and ball.distance(l_paddel) <= 50):
        ball.x_move *= -1
        default_sleep *= 0.9

    # ball miss paddels
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.x_move *= -1
        default_sleep = 0.1
        score.lpoint()
    elif ball.xcor() <-390:
        ball.goto(0,0)
        ball.x_move *= -1
        default_sleep = 0.1
        score.rpoint()
        





 
screen.exitonclick()


# capitalize() => make the first letter of the statement upper
# title() => make the first letter of each word of the statement upper
# round() => make the float to the nearest number 