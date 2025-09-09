from player import Player
from car import Car
from turtle import Screen
from lists import names
import time

### Creating Screen ###
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Turtle Froggy Game")
screen.tracer(0)

### Setting up Objects in the game ###
player = Player()
cars = []

for name in names:
    car = Car(name)
    cars.append(car)

### Game loop ###
game_is_on = True
while game_is_on:
    time.sleep(0.02)
    for car in cars:
        car.move_forward()
    screen.update()

screen.exitonclick()