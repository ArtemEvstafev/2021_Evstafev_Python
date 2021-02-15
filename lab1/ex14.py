import turtle as t
import math
import time

t.shape('classic')
t.speed(10)


def go(n):
    t.forward(n)


def left(n):
    t.left(n)


def right(n):
    t.right(n)


r = 100
n = int(input())

for k in range(n):
    if n % 2 == 0:
        k1 = (k + n / 2 - 1) % n
    else:
        k1 = (k + (n - 1) / 2) % n

    t.penup()
    t.goto(r * math.cos(2 * 3.14 * k / n), r * math.sin(2 * 3.14 * k / n))
    t.pendown()
    t.goto(r * math.cos(2 * 3.14 * k1 / n), r * math.sin(2 * 3.14 * k1 / n))

input()
