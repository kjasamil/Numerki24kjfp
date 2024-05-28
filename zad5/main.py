import approximation as ap
import functions as f
from matplotlib import pyplot as plt
import numpy as np

is_function_chosen = False
chosen_function = ""
function = None

def draw(a1, b1, func_approx, func_real):
    plt.grid(True)
    x1 = np.linspace(a1, b1, 1000)
    plt.plot(x1, func_approx(x1), color='blue', label='Wielomian aproksymujący')
    plt.plot(x1, func_real(x1), color='red', label='Funkcja aproksymowana')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

while True:
    if is_function_chosen:
        print("Wybrana funkcja:", chosen_function)
    print("1. Wybierz funkcję")
    print("2. Aproksymacja wielomianem określonego stopnia")
    print("3. Aproksymacja wielomianem z określoną dokładnością")
    print("4. Wyjdź")
    choice = input("Twój wybór:")
    if choice == "1":
        print("1. f(x) = 2x + 2")
        print("2. f(x) = (1/3)x^3 + (1/2)x^2 + x + 1")
        print("3. f(x) = 3/(1 + x)")
        print("4. f(x) = sin(2x+2)")
        print("5. f(x) = 2^x + 3")
        print("6. f(x) = 3/(1 + 2^x)")
        case = input("Wybierz funkcję: ")
        if case == '1':
            function = f.func1
            chosen_function = "f(x) = 2x + 2"
            is_function_chosen = True
        if case == '2':
            function = f.func2
            chosen_function = "f(x) = (1/3)x^3 + (1/2)x^2 + x + 1"
            is_function_chosen = True
        elif case == '3':
            function = f.func3
            chosen_function = "f(x) = 3/(1 + x)"
            is_function_chosen = True
        elif case == '4':
            function = f.func4
            chosen_function = "f(x) = sin(2x+2)"
            is_function_chosen = True
        elif case == '5':
            function = f.func5
            chosen_function = "f(x) = 2^x + 3"
            is_function_chosen = True
        elif case == '6':
            function = f.func6
            chosen_function = "f(x) = 3/(1 + 2^x)"
            is_function_chosen = True
    if choice == "2" and is_function_chosen:
        a = float(input("Podaj lewą granicę aproksymacji a:"))
        b = float(input("Podaj prawą granicę aproksymacji b:"))
        n = int(input("Podaj stopień wielomianu aproksymującego:"))
        lambda_coeffs = ap.lambdas(function, a, b, n)
        approx_polynomial = lambda x: ap.approximation(lambda_coeffs, x)
        draw(a, b, approx_polynomial, function)
        print("Błąd aproksymacji:", ap.error(lambda_coeffs, function, a, b))
    if choice == "3" and is_function_chosen:
        a = float(input("Podaj lewą granicę aproksymacji a:"))
        b = float(input("Podaj prawą granicę aproksymacji b:"))
        eps = float(input("Podaj oczekiwaną dokładność aproksymacji:"))
        n, lambda_coeffs = ap.err_lambdas(function, a, b, eps)
        approx_polynomial = lambda x: ap.approximation(lambda_coeffs, x)
        draw(a, b, approx_polynomial, function)
        print("Błąd aproksymacji:", ap.error(lambda_coeffs, function, a, b))
        print("Stopień wielomianu aproksymującego:", n)
    if choice == "4":
        break
