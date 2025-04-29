from turtle import Screen
from snake import Snake
from food import Food
from countdown import Countdown
from scoreboard import Score
import time

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
def mode():
    if difficulty == "easy":
        time.sleep(.15)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            score.add_score()
            snake.add_body_part()
    elif difficulty == "medium":
        time.sleep(.10)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            score.add_score()
            snake.add_body_part()
    elif difficulty == "hard":
        time.sleep(.05)
        snake.move()
        if snake.head.distance(food) < 20:
            food.refresh()
            score.add_score()
            snake.add_body_part()


while game_on:
    screen.update()
    mode()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
        score.try_again()
    screen.update()


screen.exitonclick()

