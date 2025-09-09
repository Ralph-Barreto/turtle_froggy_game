from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.goto( x=0 , y=-280 )
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.setheading(90)