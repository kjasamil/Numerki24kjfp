def bisection_eps(a, b, eps, func):
    center = 0
    i = 0
    if func(a) * func(b) < 0:
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
    return


def bisection_iter(a, b, iterations, func):
    center = 0
    i = 0
    if func(a) * func(b) < 0:
        while i < iterations:
            i += 1
            center = (a + b) / 2
            if func(center) == 0:
                return [center, i]
            if func(a) * func(center) < 0:
                b = center
            else:
                a = center
        return [center, i]
    return
