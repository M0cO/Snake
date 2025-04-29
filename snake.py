from turtle import Turtle
STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.tail_growth = []
        self.body()
        self.head = self.tail_growth[0]

    def body(self):
        for i in range(0, 3):
            turtle = Turtle(shape="square")
            turtle.shapesize(stretch_wid=.95,stretch_len=.95)
            turtle.penup()
            turtle.color("white")
            turtle.goto(0 - (i * 20), 0)
            self.tail_growth.append(turtle)

    def move(self):
        for tail_num in range(len(self.tail_growth) - 1, 0, -1):
            new_x = self.tail_growth[tail_num - 1].xcor()
            new_y = self.tail_growth[tail_num - 1].ycor()
            self.tail_growth[tail_num].goto(new_x, new_y)
        self.head.forward(STEPS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
