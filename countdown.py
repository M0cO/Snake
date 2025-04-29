from turtle import Turtle, Screen
import time

class Countdown(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("Green")
        self.goto(0, 200)

        self.screen = Screen()

        self.do_countdown()

    def do_countdown(self):
        for i in range(3, 0, -1):
            self.clear()
            self.write(f"{i}", align="center", font=("Arial", 36, "bold"))
            self.screen.update()
            time.sleep(1)

        self.clear()
        self.write("GO!", align="center", font=("Arial", 36, "bold"))
        self.screen.update()
        time.sleep(0.5)
        self.clear()
        self.screen.update()