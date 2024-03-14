import polynomials as p
import bisection as bi
import newton as n
from matplotlib import pyplot as plt
import numpy as np
from math import sin, cos, tan, pi
from functools import partial
POLYNOMIAL = [1, -2**0.5, -1, -3]

# print("Witaj!")
# print("Aktualnie wybrana funkcja:")
# print("Wielomian: ")
# print(p.print_polynomial(POLYNOMIAL))
# print(b.bisection_eps(2, 4, 0.0000001, POLYNOMIAL))
# print(b.bisection_eps(-1, 1, 0.0000001, POLYNOMIAL))
# print(b.bisection_iter(2, 4, 5, POLYNOMIAL))
# print(b.bisection_iter(2, 4, 10, POLYNOMIAL))
# print(p.horner_differential(0.47, POLYNOMIAL))

a = 2
b = 4
eps = 0.0000001
x = np.linspace(a, b)

# plt.plot(x, p.horner(x, POLYNOMIAL))
plt.grid(True)
# plt.show()

x = 3
print(p.horner_differential(x, POLYNOMIAL))
print(p.derivative_by_definition(x, POLYNOMIAL))
print(n.newton_eps(-1, pi, 0.00001, sin))
while True:
    print("Wybierz funkcję: ")
    print("1. Wielomian")
    print("2. Trygonometryczna")
    print("3. Wykładnicza")
    print("4. Złożenie")
    print("5. Koniec")
    case = input("Enter a number: ")
    if case == "1":
        coeffs = input("Enter coefficients: ")
        coeff_table = coeffs.split(", ")
        coeff_table = list(map(float, coeff_table))
        a = 1
        b = 1
        func = partial(p.horner, polynomial_coeffs=coeff_table)
        while func(a) * func(b) > 0:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))

        print("1. Wariant o określonej dokładności")
        print("2. Wariant o określonej liczbie iteracji")
        method = input("Wybierz wariant:")
        if method == "1":
            eps = float(input("Podaj dokładność: "))
            # bisection_eps = bi.bisection_eps(a, b, eps, coeff_table)
            newton_eps = n.newton_eps(a, b, eps, func)
            print(newton_eps)
        else:
            iterations = int(input("Podaj liczbe iteracji: "))
            # bisection_iter = bi.bisection_iter(a, b, iterations, coeff_table)
            newton_iter = n.newton_iteration(a, b, iterations, func)
            print(newton_iter)

        x = np.linspace(a, b)
        plt.plot(x, p.horner(x, coeff_table))
        plt.show()
    elif case == "2":
        print("1. Sinus")
        print("2. Cosinus")
        function = input("3. Tangens ")
        if function == "1":
            func = sin
        elif function == "2":
            func = cos
        else:
            func = tan
        a = 1
        b = 1
        while func(a) * func(b) > 0:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))

        print("1. Wariant o określonej dokładności")
        print("2. Wariant o określonej liczbie iteracji")
        method = input("Wybierz wariant:")
        if method == "1":
            eps = float(input("Podaj dokładność: "))
            # bisection_eps = bi.bisection_eps(a, b, eps, func)
            newton_eps = n.newton_eps(a, b, eps, func)
            print(newton_eps)
        else:
            iterations = int(input("Podaj liczbe iteracji: "))
            # bisection_iter = bi.bisection_iter(a, b, iterations, func)
            newton_iter = n.newton_iteration(a, b, iterations, func)
            print(newton_iter)


    break