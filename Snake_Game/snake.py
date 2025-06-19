from turtle import Turtle
CORDS = [(0,0),(-20,0),(-40,0)] # default size of square is 20x20 for turtle shape
MOVE_DISTANCE =20
class Snake:

    def __init__(self):
        """--constructor to initialize snake body list--"""
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """--creating the initial snake body--"""
        for position in CORDS:
           self.add_segments(position)

    def add_segments(self,position):
        tim = Turtle('square')
        tim.speed(20)
        tim.penup()
        tim.color('white')
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        """--automatically moves the snake without breaking the body--"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # start=2 , stop=0 , step=-1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
           self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
           self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
           self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
           self.segments[0].setheading(0)
