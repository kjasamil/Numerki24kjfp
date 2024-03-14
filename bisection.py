import polynomials as p


def bisection_poly_eps(a, b, eps, coeffs):
    center = 0
    i = 0
    if p.horner(a, coeffs) == 0:
        return [a, i]
    elif p.horner(b, coeffs) == 0:
        return [b, i]
    elif p.horner(a, coeffs) * p.horner(b, coeffs) < 0:
        while abs(a - b) > eps:
            i += 1
            center = (a + b) / 2
            if center == 0:
                return [center, i]
            if p.horner(a, coeffs) * p.horner(center, coeffs) < 0:
                b = center
            else:
                a = center
        return [center, i]
    else:
        return "Oops"


def bisection_poly_iter(a, b, iterations, coeffs):
    center = 0
    i = 0
    if p.horner(a, coeffs) == 0:
        return [a, 0]
    elif p.horner(b, coeffs) == 0:
        return [b, 0]
    elif p.horner(a, coeffs) * p.horner(b, coeffs) < 0:
        while i < iterations:
            i += 1
            center = (a + b) / 2
            if p.horner(center, coeffs) == 0:
                return [center, i]
            if p.horner(a, coeffs) * p.horner(center, coeffs) < 0:
                b = center
            else:
                a = center
        return [center, i]
    else:
        return "Oops"


def bisection_eps(a, b, eps, func):
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


def bisection_iter(a, b, iterations, func):
    center = 0
    i = 0
    if func(a) == 0:
        return [a, i]
    elif func(b) == 0:
        return [b, i]
    elif func(a) * func(b) < 0:
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
    else:
        return "Oops"