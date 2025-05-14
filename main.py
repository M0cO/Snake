from turtle import Screen
from snake import Snake
from food import Food
from countdown import Countdown
from scoreboard import Score
import time

def the_game():
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.add_body_part()

def mode():
    if difficulty == "easy":
        time.sleep(EASY)
        the_game()
    elif difficulty == "medium":
        time.sleep(MEDIUM)
        the_game()
    elif difficulty == "hard":
        time.sleep(HARD)
        the_game()

EASY = .15
MEDIUM = .10
HARD = .05

screen = Screen()
difficulty = screen.textinput("Difficulty", "Select Difficulty: Easy, Medium, or Hard").lower()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
countdown = Countdown()
score = Score()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True

while game_on:
    screen.update()
    mode()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for tail_growth in snake.tail_growth[2:]:
        if snake.head.distance(tail_growth) < 10:
            score.reset()
            snake.reset()


    screen.update()


screen.exitonclick()
