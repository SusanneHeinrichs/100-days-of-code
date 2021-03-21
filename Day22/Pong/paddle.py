from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape('square')
        self.goto(x_pos, 0)
        self.color('white')
        self.penup()
        self.shapesize(5, 1)

    def go_up(self):
        current_y = self.ycor()
        self.sety(current_y + 10)

    def go_down(self):
        current_y = self.ycor()
        self.sety(current_y - 10)



