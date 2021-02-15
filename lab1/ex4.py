import turtle as t

t.shape('turtle')


def go():
    t.forward(1)


def left():
    t.left(1)


def right():
    t.right(90)


def fig(n=3, a=50):
    for i in range(0, n):
        left(180 - (n - 2) * 180 / n)
        go(a)


for n in range(0, 360):
    go()
    left()

input()
