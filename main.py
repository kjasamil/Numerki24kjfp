import polynomials as p
import bisection as bi
import newton as n
from matplotlib import pyplot as plt
import numpy as np
from functools import partial


def exponential(xi, base_val, param):
    return base_val ** xi + param


def complex_func(xi):
    return np.sin(3*(xi**2)-2*xi)


def draw(a1, b1, func1, zero_place_display_bisection, zero_place_display_newton, one_zero_point_display,
         tan, point_bisection=0.0, point_newton=0.0, point_solo=0.0):
    plt.grid(True)
    x1 = np.linspace(a1, b1, 1000)
    plt.plot(x1, func1(x1))
    if tan:
        plt.ylim(-8, 8)
    if zero_place_display_bisection:
        plt.scatter(point_bisection, 0, color="red", label="Bisekcja")
    if zero_place_display_newton:
        plt.scatter(point_newton, 0, color="green", label="Newton")
    if one_zero_point_display:
        plt.scatter(point_solo, 0, color="blue")
    if zero_place_display_bisection or zero_place_display_newton:
        plt.legend()
    plt.show()


chosen_func_string = ""
is_chosen = False
is_chosen_tan = False
while True:
    if is_chosen:
        print("Wybrana funkcja:", chosen_func_string)
    print("1. Funkcja wielomianowa")
    print("2. Funkcja trygonometryczna")
    print("3. Funkcja wykładnicza")
    print("4. Złożenie funkcji")
    print("5. Pokaż wykres funkcji")
    print("6. Znajdź miejsce zerowe")
    print("7. Koniec")
    case = input("Wybierz opcję: ")
    if case == "1":
        coeff_table = []
        polynomial_degree = int(input("Wprowadź stopień wielomianu: "))
        if polynomial_degree > 0:
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
            is_chosen_tan = False
        else:
            print("Stopień wielomianu musi być dodatnią liczbą całkowitą.")
    elif case == "2":
        error = False
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
        elif function == "3":
            func = np.tan
            chosen_func_string = "tan(x)"
            is_chosen_tan = True
        else:
            print("Brak takiej opcji w menu.")
            error = True
        if not error:
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
        is_chosen_tan = False
    elif case == "4":
        func = complex_func
        chosen_func_string = "sin(3x^2-2x)"
        is_chosen = True
        is_chosen_tan = False
    elif case == "5":
        if is_chosen:
            a = float(input("Podaj lewy kraniec przedziału:"))
            b = float(input("Podaj prawy kraniec przedziału:"))
            if a < b:
                draw(a, b, func, False, False,
                     False, is_chosen_tan)
            else:
                print("Wybrano niewłaściwy przedział.")
        else:
            print("Brak wybranej funkcji.")
    elif case == "6":
        if is_chosen:
            print("Miejsce zerowe będzie poszukiwane na przedziale [a; b]")
            a = float(input("Podaj a: "))
            b = float(input("Podaj b: "))
            if a >= b:
                print("Wybrano niewłaściwy przedział.")
            elif func(a) * func(b) > 0:
                print("Nie jest możliwe znalezienie miejsca zerowego w tym przedziale, ponieważ f(a) * f(b) > 0.")
            elif func(a) * func(b) == 0:
                print("Bez korzystania z algorytmów można już wskazać, że:")
                if func(a) == 0:
                    zerowe = a
                else:
                    zerowe = b
                print(f"Miejsce zerowe funkcji jest w punkcie ({zerowe}, 0)")
                draw(zerowe-3, zerowe+3, func, False, False,
                     True, is_chosen_tan, 0.0, 0.0, zerowe)
            else:
                newton_ok = False
                error = False
                print("1. Wariant o określonej dokładności")
                print("2. Wariant o określonej liczbie iteracji")
                method = input("Wybierz wariant:")
                if method == "1":
                    eps = float(input("Podaj dokładność: "))
                    if eps > 0:
                        bisection = bi.bisection_eps(a, b, eps, func)
                        newton = n.newton_eps(a, b, eps, func)
                    else:
                        print("Dokładność musi być liczbą większą od 0.")
                        error = True
                else:
                    iterations = int(input("Podaj liczbę iteracji: "))
                    if iterations > 0:
                        bisection = bi.bisection_iter(a, b, iterations, func)
                        newton = n.newton_iteration(a, b, iterations, func)
                    else:
                        print("Liczba iteracji musi być liczbą całkowitą większą od 0.")
                        error = True
                if not error:
                    print("Metodą bisekcji [miejsce zerowe, ilość iteracji]: ", bisection[0], ", ", bisection[1])
                    miejsce1 = bisection[0]
                    newton_ok = (newton[2] == 1)
                    if newton_ok:
                        print("Metodą Newtona [miejsce zerowe, ilość iteracji]: ", newton[0], ", ", newton[1])
                        miejsce2 = newton[0]
                    else:
                        print("Metoda Newtona: Podczas obliczeń otrzymano punkt, w której pochodna jest zerowa."
                              "Nie jest możliwe w takiej sytuacji znalezienie miejsca zerowego.")
                    draw(a, b, func, True, newton_ok,
                         False, is_chosen_tan, miejsce1, miejsce2, 0.0)
        else:
            print("Brak wybranej funkcji.")
    elif case == "7":
        break
