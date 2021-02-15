import random as r
import turtle as t

number_of_turtles = 25
steps_of_time_number = 100

t.penup()
t.goto(-300, 0)
t.pendown()
t.goto(-300, -300)
t.goto(300, -300)
t.goto(300, 300)
t.goto(-300, 300)
t.goto(-300, 0)
t.hideturtle()

pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(100)
    unit.goto(r.randint(-300, 300), r.randint(-300, 300))

for i in range(steps_of_time_number):
    for unit in pool:
        unit.left(r.randint(0, 360))
        unit.forward(15)
        a = unit.xcor() <= -300.0 or unit.xcor() >= 300.0 or unit.ycor() <= -300.0 or unit.ycor() >= 300.0
        if a:
            unit.left(180)
            unit.forward(10)
