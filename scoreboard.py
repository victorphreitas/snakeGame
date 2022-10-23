from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 225)
        self.score = -1

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", font=("Arial", 14, "normal"), align="center")









