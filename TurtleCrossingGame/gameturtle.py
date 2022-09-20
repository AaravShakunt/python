from turtle import Turtle

class GameTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
        self.color("green")
        self.shape("turtle")
        self.shapesize(stretch_wid=2)
    
    def up(self):
        self.forward(10)
