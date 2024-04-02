

def derivative_by_definition(x, function):
    h = 1e-9
    return (function(x + h) - function(x)) / h


def newton_eps(a, b, eps, function):
    if function(a) * function(b) > 0:
        return
    x = a
    old_x = a + 2 * eps
    iteration = 0
    while abs(old_x - x) > eps:
        old_x = x
        derivative = derivative_by_definition(old_x, function)
        x = old_x - function(old_x) / derivative
        iteration = iteration + 1
    return [x, iteration]


def newton_iteration(a, b, iterations, function):
    if function(a) * function(b) > 0:
        return
    x = a
    iteration = 0
    while iterations > iteration:
        old_x = x
        derivative = derivative_by_definition(old_x, function)
        if derivative == 0:
            return [old_x, iteration]

        x = old_x - function(old_x) / derivative
        iteration = iteration + 1
        if x == old_x:
            return [x, iteration]
    return [x, iteration]
