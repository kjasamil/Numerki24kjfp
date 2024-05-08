# zwraca wartość funkcji podcałkowej w postaci znormalizowanej, tzn. gdy przedział całkowania to [-1;1]

def normalize(a, b, function, x):
    argument = lambda t: 0.5*((b - a) * t + (b + a))
    coefficient = 0.5 * (b - a)
    return coefficient * function(argument(x))


def func(x):
    return x**2 + 2


print(normalize(1,5,func,1))