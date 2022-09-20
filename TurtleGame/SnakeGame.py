from turtle import Screen, Turtle
import time
from Snake import Segments, Snake
from food import Food
from scoreboard import Scorekeep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scorekeep()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.movement()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_point()
    
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        # game_is_on = False
        scoreboard.clear()
        scoreboard.reset()
        snake.reset()
    
    for segment in snake.segments[1:]:
        # if segment == snake.segments[0]:
        #     pass

        if snake.segments[0].distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()





screen.exitonclick()