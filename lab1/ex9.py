import turtle as t
import math as m

t.shape('turtle')


def go(n):
    t.forward(n)


def left(n):
    t.left(n)


def right(n):
    t.right(n)


def fig(n=3, a=50):
    for i in range(0, n):
        left(180 - (n - 2) * 180 / n)
        go(a)


t.speed(3)
n = 3
a = 10
R = 10 / 3 ** 0.5

while n <= 12:
    fig(n, a)
    n += 1

    R += 5
    right(45)
    t.penup()
    go(5)
    t.pendown()
    left(45)
    a = 2 * R * m.sin(m.radians(360 / 6))

input()
