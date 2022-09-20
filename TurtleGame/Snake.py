from turtle import Turtle, Screen
import time

starting_positions = [(0,0), (-20,0), (-40,0)]

Segments = []


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.movement()
        
        
    def create_snake(self):
        for position in starting_positions:
            Segment = Turtle()
            Segment.penup()
            Segment.shape("square")
            Segment.color("white")
            Segment.goto(position)
            self.segments.append(Segment)
    
    def movement(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        
    def up(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].seth(90)

    def down(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].seth(270)

    def left(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].seth(180)

    def right(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].seth(0)

    def add_segment(self, position):
        Segment = Turtle()
        Segment.penup()
        Segment.shape("square")
        Segment.color("white")
        Segment.goto(position)
        self.segments.append(Segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        
