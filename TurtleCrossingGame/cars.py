from turtle import Turtle
import random

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.game_is_on = True
        self.speed_of_cars = 7
    
    def create_car(self):
        random_number = random.randint(1,10)
        if random_number == 1:
            new_car = Turtle()
            new_car.color(random.randint(1,255), random.randint(1,255), random.randint(1,255))
            new_car.penup()
            new_car.goto(350, random.randint(-250,250))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            self.all_cars.append(new_car)
        else:
            pass

    def movement_and_eliminate(self, turt, level):
        for carz in self.all_cars:
            carz.forward(self.speed_of_cars + (level*2))
            if carz.distance(turt) < 30:
                self.game_is_on = False



