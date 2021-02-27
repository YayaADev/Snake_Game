from turtle import Turtle

FONT = ("Comic Sans MS", 16, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

# def game_over(self):
#     self.goto(x=0, y=0)
#     self.pendown()
#     self.write(f"Game Over!\n Your total score is {self.score}", align=ALIGNMENT, font=FONT)
