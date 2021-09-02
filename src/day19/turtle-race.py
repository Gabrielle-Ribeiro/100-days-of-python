from turtle import Screen, Turtle
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_answer = screen.textinput(title="Make your bet", 
                                prompt="Which turtle will win the race? Enter a color:")

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_ninja_turtles = []

for turtle_index in range(0, 6):
    ninja_turtle = Turtle(shape="turtle")
    ninja_turtle.color(colours[turtle_index])
    ninja_turtle.penup()
    ninja_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_ninja_turtles.append(ninja_turtle)

if user_answer:
    is_race_on = True

while is_race_on:

    for turtle in all_ninja_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_answer:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
                

        random_distance = random.randint(0, 5)
        turtle.forward(random_distance)


screen.exitonclick()


