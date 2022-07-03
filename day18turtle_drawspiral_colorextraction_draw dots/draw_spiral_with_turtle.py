from turtle import Turtle as t
from turtle import Screen
import random

tim = t()
tim.pensize(1)
tim.hideturtle()
tim.speed(7)
color =['red','yellow','purple','blue','green','pink']
direction = [0,90,180,270]
tim.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random.choice(color))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

"""

def random_color():
    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,225)
    return (r,g,b)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(4):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

draw_shape(3)
"""


screen = Screen()
screen.exitonclick()

"""
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pencolor("pale goldenrod")
timmy_the_turtle.fillcolor("dark green")
for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


"""
