import polynomials as p


def newton_eps(a, b, eps, coeffs):
    if p.horner(a, coeffs) * p.horner(b, coeffs) > 0:
        return
    x = a
    old_x = a + 2 * eps
    iteration = 0
    while abs(old_x - x) > eps:
        old_x = x
        x = old_x - p.horner(old_x, coeffs) / p.horner_differential(old_x, coeffs)
        iteration = iteration + 1
    return [x, iteration]


def newton_iteration(a, b, iterations, coeffs):
    if p.horner(a, coeffs) * p.horner(b, coeffs) > 0:
        return
    x = a
    iteration = 0
    while iterations > iteration:
        old_x = x
        derivative_value = p.horner_differential(old_x, coeffs)
        if derivative_value == 0:
            return [old_x, iteration]

        x = old_x - p.horner(old_x, coeffs) / derivative_value
        iteration = iteration + 1
    return [x, iteration]


