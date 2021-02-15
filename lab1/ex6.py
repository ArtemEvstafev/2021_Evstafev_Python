import turtle as t

t.shape('turtle')


def go(n):
    t.forward(n)


def left(n):
    t.left(n)


def right(n):
    t.right(n)


t.speed(3)
r = int(input())
a = 360 / r

for i in range(r):
    go(300)
    t.stamp()
    right(180)
    go(300)
    right(180)
    right(a)
input()
