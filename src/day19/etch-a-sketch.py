from turtle import Turtle, Screen

arrow = Turtle()
arrow.speed("fastest")
screen = Screen()

def move_forwards():
    arrow.forward(5)

def move_backwards():
    arrow.backward(5)

def turn_left():
    new_heading = arrow.heading() + 18
    arrow.setheading(new_heading)

def turn_right():
    new_heading = arrow.heading() - 18
    arrow.setheading(new_heading)

def clear():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()