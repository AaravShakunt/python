from turtle import Turtle
from Snake import *

ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")

class Scorekeep(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        with open("TurtleGame\data.txt") as Data:
            self.HighScore = int(Data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"score : {self.Score} high score : {self.HighScore}", align = ALIGNMENT, font = FONT)
        self.update_scoreboard

    def update_scoreboard(self):
        self.clear()
        self.write(f"score : {self.Score} high score : {self.HighScore}", align = ALIGNMENT, font = FONT)


    def score_point(self):
        self.Score += 1
        self.clear()
        self.write(f"score : {self.Score} high score : {self.HighScore}", align = ALIGNMENT, font = FONT)

    # def game_over(self):
    #     self.write("Game Over!", align = ALIGNMENT, font = FONT)
    
    def reset(self):
        if self.Score > self.HighScore:
            self.HighScore = self.Score
            with open("TurtleGame\data.txt", mode="w") as Data:
                Data.write(str(self.HighScore))
        self.Score = 0
        self.update_scoreboard()


