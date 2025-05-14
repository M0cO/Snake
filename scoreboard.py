from turtle import Turtle
CENTER = "center"
FONT = ("Courier", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-180,-280)
        self.updated_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}") #look here morning
        self.score = 0
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", align=CENTER, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.updated_scoreboard()

