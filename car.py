from turtle import Turtle
import random
from lists import turtle_colours
T_or_F = [True, False]

class Car(Turtle):

    def __init__(self, name):
        super().__init__()

        self.name = name
        self.shape("square")
        self.penup()

        self.speed = "fastest"

        self.x_coordinate = random.randint(0, 400)
        x_polarity = random.randint(0,1)
        if x_polarity == 0:
            self.x_coordinate *= -1

        self.y_coordinate = random.randint(0, 240)
        y_polarity = random.randint(0,1)
        if y_polarity == 0:
            self.y_coordinate *= -1

        self.goto(self.x_coordinate, self.y_coordinate)

        self.color(random.choice(turtle_colours))
        self.move_speed = random.randint(1, 3)

        direction = random.choice(T_or_F)
        if not direction:
            self.setheading(180)
        else:
            self.setheading(0)

    def move_forward(self):
        self.forward(self.move_speed)
        if -400 > self.xcor():
            self.goto(x = 400, y = self.y_coordinate)
        if 400 < self.xcor():
            self.goto(x = -400, y = self.y_coordinate)