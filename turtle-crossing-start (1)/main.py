import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move_forward,'Up')

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    for cars in car_manager.all_cars:
        if cars.distance(player) <= 20:
            game_is_on =  False
            scoreboard.over()

    if player.starting():
        player.initial_position()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
