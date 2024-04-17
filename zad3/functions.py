import horner as h
import math as m


def func1(x):
    return abs(x-2)


def func2(x):
    return h.horner(x, [1, 2, 1, 0])


def func3(x):
    return 2*m.cos(x)+m.sin(x)


def func4(x):
    return abs(m.sin(x**2)+m.cos(x))
