import polynomials as p
import bisection as bi
import newton as n
from matplotlib import pyplot as plt
import numpy as np
from functools import partial


def exponential(xi, base_val, param):
    return base_val ** xi + param


def complex_func(x):
    return np.sin(3*(x**2)-2*x)


chosen_func_string = ""
is_chosen = False
while True:
    plt.grid(True)
    if is_chosen:
        print("Wybrana funkcja:", chosen_func_string)
    print("1. Funkcja wielomianowa")
    print("2. Funkcja trygonometryczna")
    print("3. Funkcja wykładnicza")
    print("4. Złożenie funkcji")
    print("5. Pokaż wykres funkcji")
    print("6. Znajdź miejsce zerowe")
    print("7. Koniec")
    case = input("Enter a number: ")
    if case == "1":
        polynomial_degree = int(input("Wprowadź stopień wielomianu: "))
        coeff_table = []
        max_power = polynomial_degree
        for i in range(polynomial_degree + 1):
            if max_power > 0:
                print(f"Podaj współczynnik przy wyrazie x^{max_power}:", end='')
            else:
                print("Podaj wyraz wolny:", end='')
            coefficient = float(input())
            coeff_table.append(coefficient)
            max_power -= 1
        func = partial(p.horner, polynomial_coeffs=coeff_table)
        chosen_func_string = p.polynomial_to_string(coeff_table)
        is_chosen = True
    elif case == "2":
        print("1. Sinus")
        print("2. Cosinus")
        print("3. Tangens")
        function = input("Wybierz funkcję:")
        if function == "1":
            func = np.sin
            chosen_func_string = "sin(x)"
        elif function == "2":
            func = np.cos
            chosen_func_string = "cos(x)"
        else:
            func = np.tan
            chosen_func_string = "tan(x)"
        is_chosen = True
    elif case == "3":
        base = float(input("Podaj podstawę: "))
        other_param = float(input("Podaj wyraz wolny: "))
        func = partial(exponential, base_val=base, param=other_param)
        chosen_func_string = str(base) + "^x"
        if other_param > 0:
            chosen_func_string += "+" + str(other_param)
        elif other_param < 0:
            chosen_func_string += str(other_param)
        is_chosen = True
    elif case == "4":
        func = complex_func
        chosen_func_string = "sin(3x^2-2x)"
        is_chosen = True
    elif case == "5":
        a = float(input("Podaj lewy kraniec przedziału:"))
        b = float(input("Podaj prawy kraniec przedziału:"))
        x = np.linspace(a, b)
        plt.plot(x, func(x))
        plt.show()
    elif case == "6":
        a = 1
        b = 1
        while func(a) * func(b) > 0:
            print("Miejsce zerowe będzie poszukiwane na przedziale [a; b]")
            a = float(input("Podaj a: "))
            b = float(input("Podaj b: "))
            if func(a) * func(b) > 0:
                print("Na obu krańcach przedziału f(x) > 0, nie będzie możliwe znalezienie miejsca zerowego.")
                print("Wprowadź ponownie!")
            print("1. Wariant o określonej dokładności")
            print("2. Wariant o określonej liczbie iteracji")
            method = input("Wybierz wariant:")
            if method == "1":
                eps = float(input("Podaj dokładność: "))
                bisection_eps = bi.bisection_eps(a, b, eps, func)
                newton_eps = n.newton_eps(a, b, eps, func)
                print("Metodą bisekcji [miejsce zerowe, ilość iteracji]: ", bisection_eps)
                print("Metodą Newtona [miejsce zerowe, ilość iteracji]: ", newton_eps)
            else:
                iterations = int(input("Podaj liczbe iteracji: "))
                bisection_iter = bi.bisection_iter(a, b, iterations, func)
                newton_iter = n.newton_iteration(a, b, iterations, func)
                print("Metodą bisekcji [miejsce zerowe, ilość iteracji]: ", bisection_iter)
                print("Metodą Newtona [miejsce zerowe, ilość iteracji]: ", newton_iter)
            x = np.linspace(a, b)
            plt.plot(x, func(x))
            plt.show()
    elif case == "7":
        break
