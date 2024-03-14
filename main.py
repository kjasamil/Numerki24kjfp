import polynomials as p
import bisection as bi
import newton as n
from matplotlib import pyplot as plt
import numpy as np
from functools import partial
POLYNOMIAL = [1, -2**0.5, -1, -3]


def exponential(xi, base_val, param):
    return base_val ** xi + param


# print("Witaj!")
# print("Aktualnie wybrana funkcja:")
# print("Wielomian: ")
# print(p.print_polynomial(POLYNOMIAL))
plt.grid(True)
func = np.sin
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
        func = partial(p.horner, polynomial_coeffs=coeff_table)
    elif case == "2":
        print("1. Sinus")
        print("2. Cosinus")
        function = input("3. Tangens ")
        if function == "1":
            func = np.sin
        elif function == "2":
            func = np.cos
        else:
            func = np.tan
    elif case == "3":
        base = float(input("Podaj podstawę: "))
        other_param = float(input("Podaj wyraz wolny: "))
        func = partial(exponential, base_val=base, param=other_param)
    elif case == "4":
        print("TODO: not implemented")
        break
    elif case == "5":
        break

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
        bisection_eps = bi.bisection_eps(a, b, eps, func)
        newton_eps = n.newton_eps(a, b, eps, func)
        print(bisection_eps, newton_eps)
    else:
        iterations = int(input("Podaj liczbe iteracji: "))
        bisection_iter = bi.bisection_iter(a, b, iterations, func)
        newton_iter = n.newton_iteration(a, b, iterations, func)
        print(bisection_iter, newton_iter)

    x = np.linspace(a, b)
    plt.plot(x, func(x))
    plt.show()

    break
