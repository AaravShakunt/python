from turtle import Turtle, Screen
from cars import Cars
from level_tracker import Level_Tracker
from gameturtle import GameTurtle
import time


screen = Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Turtle Crossing Game")
screen.colormode(255)

turtle1 = GameTurtle()

level_tracker = Level_Tracker()

screen.listen()
screen.onkey(turtle1.up, "Up")

car = Cars()

while car.game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.movement_and_eliminate(turtle1, level_tracker.level)
    if turtle1.ycor() > 280:
        level_tracker.level_up()
        turtle1.goto(0, -280)



    

screen.exitonclick()

