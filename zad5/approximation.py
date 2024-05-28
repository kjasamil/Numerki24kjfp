import integral as itg
import laguerre as lg
import horner as h
import math as m
import numpy as np
from matplotlib import pyplot as plt

INTEGRAL_ERROR = 0.0000001  # błąd do całkowania Simpsonem

def lambdas(function, a, b, n):
    coefficients = []
    for k in range(n + 1):
        laguerre_coeffs = lg.laguerre(k)  # pobieramy współczynniki k-tego wielomianu laguerra
        # poniżej funkcja podcałkowa do licznika (slajd 24)
        numerator_function = lambda x: m.exp(-x) * function(x) * h.horner(x, laguerre_coeffs)
        # a tu funkcja podcałkowa do mianownika (slajd 24)
        denominator_function = lambda x: m.exp(-x) * h.horner(x, laguerre_coeffs)**2
        # poniżej liczymy całki
        numerator_integral = itg.integral(numerator_function, a, b, INTEGRAL_ERROR)
        denominator_integral = itg.integral(denominator_function, a, b, INTEGRAL_ERROR)
        # tutaj dalej wzór ze slajdu 24 (linijka poniżej), obliczyliśmy to c_k
        coefficient = numerator_integral / denominator_integral
        coefficients.append(coefficient)
    return coefficients


def error(l_c, function, a, b):  # błąd jako norma L2 z wagą e^-x
    error_func = lambda x: m.exp(-x) * (function(x) - approximation(l_c, x))**2
    error_int = itg.integral(error_func, a, b, INTEGRAL_ERROR)
    return m.sqrt(error_int)


def err_lambdas(function, a, b, eps):
    i = 1
    while True:
        new_coefficients = lambdas(function, a, b, i)
        new_err = error(new_coefficients, function, a, b)
        if i > 1 and new_err > old_err:
            chosen_coeffs = old_coefficients
            n = i - 1
            break
        if new_err < eps:
            chosen_coeffs = new_coefficients
            n = i
            break
        old_err = new_err
        old_coefficients = new_coefficients
        i += 1
    return [n, chosen_coeffs]


def approximation(lambdas, x):  # tu liczymy już wartości funkcji aproksymującej
    result = 0
    for i in range(len(lambdas)):
        laguerre_coeffs = lg.laguerre(i)
        result += h.horner(x, laguerre_coeffs)*lambdas[i]
    return result
