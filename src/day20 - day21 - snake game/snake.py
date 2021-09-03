from turtle import Turtle
import time

STARTING_POSITIONS = [(0,0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_body = Turtle("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(position)
            self.snake.append(snake_body)

    def move(self):
        for body_piece in range(len(self.snake)-1, 0, -1):
            new_x_position = self.snake[body_piece - 1].xcor()
            new_y_position = self.snake[body_piece - 1].ycor()
            self.snake[body_piece].goto(new_x_position, new_y_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    

