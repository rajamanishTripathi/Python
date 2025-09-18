import random
from turtle import Turtle,Screen

screen = Screen()
is_race = False
screen.setup(width=500, height=400)
userbet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race")
print(userbet)
color = ["green", "yellow", "red", "blue", "brown","violet"]
y_pos = [-70,-40,-10,20,50,80]

all_turtle = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_pos[i])
    all_turtle.append(new_turtle)

if userbet:
    is_race = True

while is_race:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race = False
            winning = turtle.pencolor()
            if winning == userbet:
                print(f"You Won.")
            else:
                print(f"You Lose. The winning turtle is {winning}")
        randist = random.randint(0,10)
        turtle.forward(randist)

screen.exitonclick()