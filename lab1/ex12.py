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
        if i == n / 2:
            break
        right(180 - (n - 2) * 180 / n)
        go(a)


left(90)
for i in range(20):
    figR(200, 1)
    figR(200, 0.3)
