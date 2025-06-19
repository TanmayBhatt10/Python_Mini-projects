from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple","cyan","pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CORDS = [20,50,100,150,-45,-90,-150,-20]

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
           new_car = Turtle('square')
           new_car.shapesize(1,2)
           new_car.penup()
           new_car.color(random.choice(COLORS))
           random_y = random.randint(-250,250)
           new_car.goto(300,random_y)
           self.all_cars.append(new_car)

    def move_cars(self):
        for i in self.all_cars:
            i.backward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
