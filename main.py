def func(x, opt=2):
    if opt == 1:
        return x * (x * (x - 2) - 2) - 3
    if opt == 2:
        return x * (x * (x - 2 ** 0.5) - 1) - 3


def bisection_eps(a, b, eps):
    center = 0
    i = 0
    if func(a) == 0:
        return [a, i]
    elif func(b) == 0:
        return [b, i]
    elif func(a) * func(b) < 0:
        while abs(a - b) > eps:
            i += 1
            center = (a + b) / 2
            if func(center) == 0:
                return [center, i]
            if func(a) * func(center) < 0:
                b = center
            else:
                a = center
        return [center, i]
    else:
        return "Oops"

def bisection_iter(a, b, iter):
    center = 0
    i = 0
    if func(a) == 0:
        return [a, 0]
    elif func(b) == 0:
        return [b, 0]
    elif func(a) * func(b) < 0:
        while i < iter:
            i += 1
            center = (a + b) / 2
            if func(center) == 0:
                return [center, i]
            if func(a) * func(center) < 0:
                b = center
            else:
                a = center
        return [center, i]
    else:
        return "Oops"


print(bisection_eps(2, 4, 0.0000001))
print(bisection_eps(-1, 1, 0.0000001))
print(bisection_iter(2, 4, 5))
print(bisection_iter(2, 4, 10))
