import turtle as t

t.shape('turtle')


def go(n):
    t.forward(n)


def left():
    t.left(90)


def right():
    t.right(90)


n = 50
for r in range(0, 10):
    for i in range(0, 4):
        go(n)
        left()
    right()
    t.penup()
    go(20)
    t.pendown()
    right()
    go(20)
    right()
    right()
    n += 40

input()
