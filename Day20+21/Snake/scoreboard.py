from turtle import Turtle
FONT = ("Arial", 24 , "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode = "r") as file:
            self. highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.highscore}", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode= "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
