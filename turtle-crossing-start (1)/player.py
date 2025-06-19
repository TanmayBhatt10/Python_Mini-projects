from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.initial_position()

    def initial_position(self):
        self.goto(STARTING_POSITION)

    def move_forward(self):
        if self.ycor() < FINISH_LINE_Y:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def starting(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
