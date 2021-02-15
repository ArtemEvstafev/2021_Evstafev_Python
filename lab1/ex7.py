import turtle as t

t.shape('turtle')


def go(n):
    t.forward(n)


def left(n):
    t.left(n)


def right():
    t.right(90)


t.speed(25)
n = 0.1
while True:
    for i in range(0, 180):
        go(n)
        left(1)
    n += 0.1

input()
