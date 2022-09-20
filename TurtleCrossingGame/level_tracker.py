from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")

class Level_Tracker(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"LEVEL : {self.level}", align = ALIGNMENT, font = FONT)
        self.update_scoreboard
        self.game_is_on = True
        self.round_is_on = True

    def update_scoreboard(self):
        self.write(f"LEVEL : {self.level}", align = ALIGNMENT, font = FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL : {self.level}", align = ALIGNMENT, font = FONT)


    # def game_over(self):
    #     if self.ScoreL > 6:
    #         self.write("LEFT SIDE HAS WON!", align = ALIGNMENT, font = FONT)
    #         self.game_is_on = False
    #     if self.ScoreR > 6:
    #         self.write("RIGHT SIDE HAS WON!", align = ALIGNMENT, font = FONT)
    #         self.game_is_on = False