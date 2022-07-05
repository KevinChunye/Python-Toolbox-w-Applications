from turtle import Turtle
Alignment = "center"
FONT = ("Courier",24,"normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score:{self.score}", align=Alignment, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over, Your Total Score is {self.score}", align="center", font=("Arial", 24, "normal"))

