from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("------MY SNAKE GAME 🐍------")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

move = True
while move:
    screen.update()
    time.sleep(0.1)
    snake.move()
    """detect collision with food"""
    if snake.segments[0].distance(food) < 15:
         food.refresh()
         snake.extend()
         score.increase_score()
    """detect wall collision"""
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
         score.gameover()
         move = False
    """detect collision with tail"""
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            move = False
            score.gameover()

screen.exitonclick()
