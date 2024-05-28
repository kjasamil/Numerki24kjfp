import numpy as np
from matplotlib import pyplot as plt

import integral as itg
import laguerre as lg
import horner as h


def sum_weight_times_laguerre(coefficients):
    max_degree = max(len(p) for p in coefficients) - 1  # kod od tej linijki i poniżej ma być odpowiedzialny za to
    result = [0.0] * (max_degree + 1)  # żeby z tablic współczynników w coefficients utworzyć
    for poly in coefficients:  # jedną tablicę z współczynnikami jednego wielomianu który
        degree = len(poly) - 1  # jest sumą wielomianów z tablic
        for i, coeff in enumerate(poly):  # czyli jak mamy coefficients = [[1.0], [-1.0,1.0]]
            result[max_degree - (degree - i)] += coeff  # to result = [-1.0, 2.0]
    return result


def plot_error_coeffs(fun, a, b, coeffs):
    final_poly = sum_weight_times_laguerre(coeffs)
    x_lin = np.linspace(a, b, 100)
    poly_error = np.sqrt(np.mean(h.horner(x_lin, final_poly) - fun(x_lin)) ** 2)
    plt.plot(x_lin, h.horner(x_lin, final_poly))
    plt.plot(x_lin, fun(x_lin), color='red')
    plt.title('Laguerre at home:')
    plt.show()
    return poly_error, final_poly


def iter_approximation(function, a, b, n):
    laguerre_coeffs = []
    for k in range(n):
        laguerre_poly = np.array(lg.laguerre(k))
        integral = lambda x: function(x) * h.horner(x, laguerre_poly) * np.exp(-x)
        coeff = itg.integral(integral, a, b, 1e-5)
        laguerre_coeffs.append(laguerre_poly * coeff)

    return n, plot_error_coeffs(function, a, b, laguerre_coeffs)


def err_approximation(function, a, b, error):
    laguerre_coeffs = []
    poly_error = 2 * error
    k = 0
    x_lin = np.linspace(a, b, 100)
    while poly_error > error:
        laguerre_poly = np.array(lg.laguerre(k))
        integral = lambda x: function(x) * h.horner(x, laguerre_poly) * np.exp(-x)
        coeff = itg.integral(integral, a, b, 1e-5)
        laguerre_coeffs.append(laguerre_poly * coeff)
        k += 1
        if np.any(abs(laguerre_coeffs[-1]) < 1e-42) and np.any(abs(laguerre_coeffs[-1]) > 0):
            break

        final_poly = sum_weight_times_laguerre(laguerre_coeffs)
        poly_error = np.sqrt(np.mean(h.horner(x_lin, final_poly) - func(x_lin)) ** 2)

    return k, plot_error_coeffs(function, a, b, laguerre_coeffs)


def format_output(data):
    return f"\nIteracja: {data[0]}, błąd aproksymacji: {data[1][0]}, współczynniki:\n {data[1][1]}"


def func(x):
    return 2 * x ** 3 - 4 * x ** 2 + 8 * x - 3


print(format_output(iter_approximation(func, 1, 5, 20)))

print(format_output(err_approximation(func, 1, 5, 0.1)))
