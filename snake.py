from turtle import Turtle
STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START = (40,0),(20,0),(60,0)

class Snake:
    def __init__(self):
        self.tail_growth = []
        self.body()
        self.head = self.tail_growth[0]

    def body(self):
        for position in START:
           self.body_part(position)

    def body_part(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.tail_growth.append(new_segment)

    def reset(self):
        for seg in self.tail_growth:
            seg.goto(1000,1000)
        self.tail_growth.clear()
        self.body()
        self.head = self.tail_growth[0]


    def add_body_part(self):
        self.body_part(self.tail_growth[-1].position())

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


