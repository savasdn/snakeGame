from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write("Game Over!", align= ALIGNMENT, font=("Courier", 48, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
