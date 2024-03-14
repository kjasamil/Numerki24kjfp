import polynomials as p
import bisection as bi
import newton as n
from matplotlib import pyplot as plt
import numpy as np
from math import sin, cos, tan, pi

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
        while p.horner(a, coeff_table) * p.horner(b, coeff_table) > 0:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))

    print("1. Wariant o określonej dokładności")
    print("2. Wariant o określonej liczbie iteracji")
    method = input("Wybierz wariant:")
    if method == "1":
        eps = float(input("Podaj dokładność: "))
        bisection_eps = bi.bisection_eps(a, b, eps, coeff_table)
        newton_eps = n.newton_eps(a, b, eps, coeff_table)
        print(bisection_eps, newton_eps)
    else:
        iterations = int(input("Podaj liczbe iteracji: "))
        bisection_iter = bi.bisection_iter(a, b, iterations, coeff_table)
        newton_iter = n.newton_iteration(a, b, iterations, coeff_table)
        print(bisection_iter, newton_iter)

    x = np.linspace(a, b)
    plt.plot(x, p.horner(x, coeff_table))
    plt.show()

    break