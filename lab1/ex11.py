import turtle as t

t.shape('turtle')
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


n = 1
left(90)
for i in range(0, 10):
    figR(200, n)
    figL(200, n)
    n += 0.5

input()
