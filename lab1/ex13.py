import turtle as t

t.shape('classic')
t.speed(0)


def go(n):
    t.forward(n)


def left(n):
    t.left(n)


def right(n):
    t.right(n)


def figL(n, a):
    for i in range(0, n):
        left(180 - (n - 2) * 180 / n)
        go(a)


def figR(n, a):
    for i in range(0, n):
        right(180 - (n - 2) * 180 / n)
        go(a)


def figN(n, a):
    for i in range(0, n):
        if i == n / 2:
            break
        right(180 - (n - 2) * 180 / n)
        go(a)


# face
t.color('yellow')
t.begin_fill()
figR(300, 2)
t.end_fill()
# eyes
t.color('blue')
right(90)
t.penup()
go(45)
left(90)
go(45)
t.pendown()
t.begin_fill()
figR(60, 1)  # first one
t.end_fill()
left(180)
t.penup()
go(90)
t.pendown()
t.begin_fill()
figL(60, 1)  # second one
t.end_fill()
t.penup()
left(180)
go(45)
right(90)
go(45)
t.pendown()
t.width(9)
t.color('black')
go(30)  # nose
t.penup()
go(20)
left(90)
go(40)
t.color('red')
t.pendown()
right(90)
figN(250, 1)

input()
