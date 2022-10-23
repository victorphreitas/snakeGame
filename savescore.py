from turtle import Turtle
from scoreboard import Scoreboard

class Savescore(Turtle):

    def __init__(self):
        current_score = Scoreboard()
        self.total = current_score.score