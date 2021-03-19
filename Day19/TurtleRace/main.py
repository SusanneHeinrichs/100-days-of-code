from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race?Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_start= -100
all_turtles = []

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y_start)
    y_start += 40
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You loose! The {winning_color} turtle is the winner!")
        rand_dist = randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
