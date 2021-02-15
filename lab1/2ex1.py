import turtle as t
import random as r

t.speed(10)
for i in range(0, 100):
    t.forward(r.randint(0, 100))
    t.left(r.randint(0, 360))
