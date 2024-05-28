import numpy as np
from matplotlib import pyplot as plt
from numpy.polynomial.laguerre import lagfit, lagval

import integral as itg
import laguerre as lg
import horner as h


def approximation(function, a, b, n):
    integral_error = 0.000001  # błąd do całkowania Simpsonem
    # tablica coefficients przechowuje tablice współczynników wielomianów laguerra wymnożonych przez poniżej
    # obliczony współczynnik coefficient (wykład slajd 37)
    # coefficient to tam c_i natomiast u nich g_i(x) to u nas i-ty wielomian laguerra
    coefficients = []
    for k in range(n + 1):
        laguerre_coeffs = lg.laguerre(k)  # pobieramy współczynniki k-tego wielomianu laguerra
        # poniżej funkcja podcałkowa do licznika (slajd 24)
        numerator_function = lambda x: function(x) * h.horner(x, laguerre_coeffs)
        # a tu funkcja podcałkowa do mianownika (slajd 24)
        denominator_function = lambda x: h.horner(x, laguerre_coeffs) * h.horner(x, laguerre_coeffs)
        # poniżej liczymy całki
        numerator_integral = itg.integral(numerator_function, a, b, integral_error)
        denominator_integral = itg.integral(denominator_function, a, b, integral_error)
        # tutaj dalej wzór ze slajdu 24 (linijka poniżej), obliczyliśmy to c_k
        coefficient = numerator_integral / denominator_integral
        for i in range(len(laguerre_coeffs)):  # wymnażamy współczynniki wielomianu laguerra przez to c_k
            print(laguerre_coeffs[i])
            laguerre_coeffs[i] *= coefficient  # slajd 37
            print(coefficient)
            print(laguerre_coeffs[i])
            print()
        print(laguerre_coeffs)
        print()
        coefficients.append(laguerre_coeffs)   # dodajemy współczynniki wielomianu do coefficients
    max_degree = max(len(p) for p in coefficients) - 1  # kod od tej linijki i poniżej ma być odpowiedzialny za to
    result = [0.0] * (max_degree + 1)                   # żeby z tablic współczynników w coefficients utworzyć
    print(coefficients)
    for poly in coefficients:                           # jedną tablicę z współczynnikami jednego wielomianu który
        degree = len(poly) - 1                          # jest sumą wielomianów z tablic
        for i, coeff in enumerate(poly):                # czyli jak mamy coefficients = [[1.0], [-1.0,1.0]]
            print(result[max_degree - (degree - i)])
            result[max_degree - (degree - i)] += coeff  # to result = [-1.0, 2.0]
            print(coeff)
        print(result)
    return result[::-1]


def func(x):
    return 2 * x ** 3 - 4 * x ** 2 + 8 * x - 3


print(itg.integral(func, 0, 10, 0.0000001))
laguerre_aprox = approximation(func, 0, 10, 3)
print(laguerre_aprox)


x_lin = np.linspace(0, 1, 100)
plt.plot(x_lin, h.horner(x_lin, laguerre_aprox))
plt.plot(x_lin, func(x_lin), color='red')
plt.title('Laguerre at home:')
plt.show()


b = lagfit(x_lin, func(x_lin), 3)
print(b)
plt.plot(x_lin, func(x_lin))
plt.plot(x_lin, lagval(x_lin, b), label='lagfit')
plt.title('Laguerre by np:')
plt.show()
