from turtle import Turtle
CENTER = "center"
FONT = ("Courier", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-240,-280)
        self.updated_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("WOMP WOMP\nGAME OVER", align=CENTER, font=FONT)

    def updated_scoreboard(self):
        self.write(f"Score: {self.score}", align=CENTER, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.updated_scoreboard()


