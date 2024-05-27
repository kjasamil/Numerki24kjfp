def get_arguments(a, b, N):
    arguments = []
    h = (b-a)/N
    for i in range(N+1):
        arguments.append(a + i * h)
    return arguments


def simpson(function, arguments):
    h = arguments[1] - arguments[0]
    N = len(arguments) - 1
    simpson_sum = 0
    for i in range(N//2):
        simpson_sum += h/3 * (function(arguments[2*i])+4*function(arguments[2*i+1])+function(arguments[2*i+2]))
    return simpson_sum


def integral(function, a, b, eps):
    number = 2
    iteration = 1
    integral = 0
    while True:
        new_integral = simpson(function, get_arguments(a, b, number))
        if iteration > 1 and abs(new_integral - integral) < eps:
            break
        integral = new_integral
        iteration += 1
        number *= 2
    return new_integral
