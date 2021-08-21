#import colorgram

#colors = colorgram.extract("src/day18 - hirst painting/image.jpg", 30)
#rgb_colors = []

#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #rgb_colors.append((r,g,b))

import turtle
import random

color_list = [(198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), 
              (238, 228, 5), (229, 159, 46), (27, 39, 158), (215, 74, 12), 
              (15, 154, 16), (199, 14, 10), (242, 247, 252), (244, 33, 165), 
              (229, 17, 122), (73, 9, 31), (60, 14, 8), (224, 141, 211), 
              (222, 160, 8), (10, 98, 61), (17, 18, 43), (47, 214, 232), 
              (11, 227, 239), (79, 72, 215), (237, 155, 222), (73, 213, 169), 
              (78, 234, 201), (50, 234, 244), (3, 66, 40)]

turtle.colormode(255)
tim = turtle.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(255)
tim.forward(250)
tim.setheading(0)


number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()