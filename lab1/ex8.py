import turtle as t

t.shape('turtle')


def go(n):
    t.forward(n)


def left():
    t.left(90)


def right():
    t.right(90)


n = 20
while True:
    go(n)
    left()
    go(n)
    left()
    n += 20
input()
