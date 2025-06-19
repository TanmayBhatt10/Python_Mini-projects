from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

score = Score()
screen = Screen()
screen.tracer(0)
screen.setup(800,600)
screen.title('----PONG Game 🏓----')
screen.bgcolor('black')
screen.listen()
ball = Ball()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.onkey(r_paddle.go_up,"1")
screen.onkey(r_paddle.go_down,"2")
screen.onkey(l_paddle.go_up,"Up")
screen.onkey(l_paddle.go_down,"Down")

on = True
while on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    """collision with wall"""
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()
    """collision with the paddle"""
    if ball.distance(r_paddle) <50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()
