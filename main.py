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


chosen_func_string = ""
is_chosen = False
is_chosen_tan = False
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
                x = np.linspace(a, b, 1000)
                plt.plot(x, func(x))
                if is_chosen_tan:
                    plt.ylim(-8, 8)
                plt.show()
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
                    print(f"Miejsce zerowe funkcji jest w punkcie ({a}, 0)")
                    zerowe = a
                else:
                    print(f"Miejsce zerowe funkcji jest w punkcie ({b}, 0)")
                    zerowe = b
                x = np.linspace(zerowe - 3, zerowe + 3, 1000)
                plt.scatter(zerowe, 0, color="red")
                plt.plot(x, func(x))
                if is_chosen_tan:
                    plt.ylim(-8, 8)
                plt.show()
            else:
                error = False
                print("1. Wariant o określonej dokładności")
                print("2. Wariant o określonej liczbie iteracji")
                method = input("Wybierz wariant:")
                if method == "1":
                    eps = float(input("Podaj dokładność: "))
                    if eps > 0:
                        bisection_eps = bi.bisection_eps(a, b, eps, func)
                        newton_eps = n.newton_eps(a, b, eps, func)
                        print("Metodą bisekcji [miejsce zerowe, ilość iteracji]: ", bisection_eps[0], ", ", bisection_eps[1])
                        if newton_eps[2] == 1:
                            print("Metodą Newtona [miejsce zerowe, ilość iteracji]: ", newton_eps[0], ", ", newton_eps[1])
                        else:
                            print("Metoda Newtona: Podczas obliczeń otrzymano punkt, w której pochodna jest zerowa."
                                  "Nie jest możliwe w takiej sytuacji znalezienie miejsca zerowego.")
                        plt.scatter(bisection_eps[0], 0, color="red")
                        if newton_eps[2] == 1:
                            plt.scatter(newton_eps[0], 0, color="green")
                    else:
                        print("Dokładność musi być liczbą większą od 0.")
                        error = True
                else:
                    iterations = int(input("Podaj liczbę iteracji: "))
                    if iterations > 0:
                        bisection_iter = bi.bisection_iter(a, b, iterations, func)
                        newton_iter = n.newton_iteration(a, b, iterations, func)
                        print("Metodą bisekcji [miejsce zerowe, ilość iteracji]: ", bisection_iter[0], ", ", bisection_iter[1])
                        if newton_iter[2] == 1:
                            print("Metodą Newtona [miejsce zerowe, ilość iteracji]: ", newton_iter[0], ", ", newton_iter[1])
                        else:
                            print("Metoda Newtona: Podczas obliczeń otrzymano punkt, w której pochodna jest zerowa."
                                  "Nie jest możliwe w takiej sytuacji znalezienie miejsca zerowego.")
                        plt.scatter(bisection_iter[0], 0, color="red")
                        if newton_iter[2] == 1:
                            plt.scatter(newton_iter[0], 0, color="green")
                    else:
                        print("Liczba iteracji musi być liczbą całkowitą większą od 0.")
                        error = True
                if not error:
                    x = np.linspace(a, b, 1000)
                    plt.plot(x, func(x))
                    if is_chosen_tan:
                        plt.ylim(-8, 8)
                    plt.show()
        else:
            print("Brak wybranej funkcji.")
    elif case == "7":
        break
