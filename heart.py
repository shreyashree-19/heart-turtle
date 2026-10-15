import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.penup()
t.color("#ffb6c1")

# Draw heart curve with text
for scale in range(11, 17):   # scaling factor loop
    for i in range(120):      # 120 points for smooth curve
        angle = (math.pi * 2) / 120 * i

        # Heart curve equations
        x = 16 * (math.sin(angle) ** 3) * scale
        y = (13 * math.cos(angle) -
             5 * math.cos(2 * angle) -
             2 * math.cos(3 * angle) -
             math.cos(4 * angle)) * scale

        t.goto(x, y)
        t.write("I love you", align="center", font=("Arial", 8, "bold"))

turtle.done()
