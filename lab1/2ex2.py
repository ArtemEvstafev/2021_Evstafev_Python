import turtle as t


def Number(num):
    n = 20
    if (num == 0):
        C0(n)
    while num > 0:
        q = num % 10
        num //= 10
        if q == 0:
            C0(n)
        elif q == 1:
            C1(n)
        elif q == 2:
            C2(n)
        elif q == 3:
            C3(n)
        elif q == 4:
            C4(n)
        elif q == 5:
            C5(n)
        elif q == 6:
            C6(n)
        elif q == 7:
            C7(n)
        elif q == 8:
            C8(n)
        elif q == 9:
            C9(n)

        t.forward(1.5 * n)
        t.right(180)
        t.pendown()


def C0(n):
    C0 = [(0, n), (90, 2 * n), (90, n), (90, 2 * n)]
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.left(90)
    t.penup()


def C1(n):
    C0 = [(225, 2 ** 0.5 * n), (135, 2 * n)]
    t.penup()
    t.right(90)
    t.forward(n)
    t.pendown()
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.left(180)
    t.forward(2 * n)
    t.left(90)
    t.penup()
    t.forward(n)


def C2(n):
    C0 = [(0, n), (90, n), (45, 2 ** 0.5 * n), (225, n)]
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.left(90)
    t.penup()
    t.forward(2 * n)
    t.left(90)
    t.forward(n)


def C3(n):
    C0 = [(0, n), (135, n * 2 ** 0.5), (225, n), (135, 2 ** 0.5 * n)]
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.right(135)
    t.penup()
    t.forward(2 * n)
    t.left(90)


def C4(n):
    C0 = [(90, n), (270, n), (90, n), (180, 2 * n)]
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.left(90)
    t.penup()
    t.forward(n)


def C5(n):
    C0 = [(0, n), (180, n), (270, n), (270, n), (90, n), (90, n)]
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.right(90)
    t.penup()
    t.forward(2 * n)
    t.left(90)


def C6(n):
    t.penup()
    t.forward(n)
    t.pendown()
    C0 = [(135, 2 ** 0.5 * n), (225, n), (90, n), (90, n), (90, n)]
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.penup()
    t.forward(n)
    t.left(90)


def C7(n):
    C0 = [(0, n), (135, n * 2 ** 0.5), (315, n)]
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.penup()
    t.left(180)
    t.forward(2 * n)
    t.left(90)


def C8(n):
    C0 = [(0, n), (90, n), (90, n), (180, n), (90, n), (90, n), (90, 2 * n)]
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.penup()
    t.left(90)


def C9(n):
    C0 = [(0, n), (90, n), (45, 2 ** 0.5 * n), (180, n * 2 ** 0.5), (225, n), (90, n)]
    for u, d in C0:
        t.right(u)
        t.forward(d)
    t.penup()
    t.left(90)


num = int(input())
Number(num)
input()
