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


def func(x):
    return x**2+3


print(simpson(func, get_arguments(0,4,4)))
