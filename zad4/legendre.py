import math

# zwraca wartość funkcji podcałkowej w postaci znormalizowanej, tzn. gdy przedział całkowania to [-1;1]


knots = [[-math.sqrt(3) / 3, math.sqrt(3) / 3],
         [-math.sqrt(15) / 5, 0, math.sqrt(15) / 5],
         [-math.sqrt(525 + 70 * math.sqrt(30)) / 35, -math.sqrt(525 - 70 * math.sqrt(30)) / 35,
          math.sqrt(525 - 70 * math.sqrt(30)) / 35, math.sqrt(525 + 70 * math.sqrt(30)) / 35, ],
         [-math.sqrt(245 + 14 * math.sqrt(70)) / 21, -math.sqrt(245 - 14 * math.sqrt(70)) / 21,
          0, math.sqrt(245 - 14 * math.sqrt(70)) / 21, math.sqrt(245 + 14 * math.sqrt(70)) / 21]]

coeffs = [[1, 1],
          [5 / 9, 8 / 9, 5 / 9],
          [(18 - math.sqrt(30)) / 36, (18 + math.sqrt(30)) / 36, (18 + math.sqrt(30)) / 36, (18 - math.sqrt(30)) / 36],
          [(322 - 13 * math.sqrt(70)) / 900, (322 + 13 * math.sqrt(70)) / 900,
           128 / 225, (322 + 13 * math.sqrt(70)) / 900, (322 - 13 * math.sqrt(70)) / 900]]


def normalize(a, b, function, x):
    argument = lambda t: 0.5 * ((b - a) * t + (b + a))
    coefficient = 0.5 * (b - a)
    return coefficient * function(argument(x))


def func(x):
    return x ** 2 + 2


def legendre(knot_number, a, b, function):
    option = knot_number - 2
    if option < 0:
        option = 0
    elif option > 3:
        option = 3
    knots_sum = 0
    my_knots = knots[option]
    my_coeffs = coeffs[option]
    for idx in range(len(my_knots)):
        knots_sum += normalize(a, b, function, my_knots[idx]) * my_coeffs[idx]
    return knots_sum
