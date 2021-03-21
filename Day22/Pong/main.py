from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)

paddle_right = Paddle(350)
paddle_left = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

middle_line = Turtle()
middle_line.goto(0, 300)
middle_line.speed("fast")
middle_line.color('white')
middle_line.setheading(270)
for i in range(0, 50):
    middle_line.forward(10)
    middle_line.penup()
    middle_line.forward(10)
    middle_line.pendown()

screen.listen()
screen.onkey(paddle_left.go_up, 'Up')
screen.onkey(paddle_left.go_down, 'Down')
screen.onkey(paddle_right.go_up, 'w')
screen.onkey(paddle_right.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < 320:
        ball.bounce_x()

    # detect right paddle misses and speed u ball after making a point 
    if ball.xcor() > 400:
        ball.reset_position()
        ball.x_move -= 1
        ball.y_move -= 1
        scoreboard.left_point()

    # detect left paddle misses and speed up ball after making a point
    if ball.xcor() < -400:
        ball.reset_position()
        ball.x_move += 1
        ball.y_move += 1
        scoreboard.right_point()

screen.exitonclick()
