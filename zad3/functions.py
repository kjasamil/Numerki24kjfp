import horner as h
import numpy as np


def func1(x):
    return 2*x+2


def func2(x):
    return abs(x-2)


def func3(x):
    return h.horner(x, [1, 2, 1, 0])


def func4(x):
    return 2*np.cos(x)+np.sin(x)


def func5(x):
    return abs(np.sin(x**2)+np.cos(x))
