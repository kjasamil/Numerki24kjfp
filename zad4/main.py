import functions as f
import legendre as leg
import simpson as simp

is_function_chosen = False
chosen_function = ""
function = None
while True:
    if is_function_chosen:
        print("Wybrana funkcja:", chosen_function)
    print("1. Wybierz funkcję")
    print("2. Całkuj za pomocą metody Simpsona")
    print("3. Całkuj za pomocą metody Gaussa-Legendre'a")
    print("4. Wyjdź")
    choice = input("Twój wybór:")
    if choice == "1":
        print("1. f(x) = 2x + 2")
        print("2. f(x) = (1/3)x^3 + (1/2)x^2 + x + 1")
        print("3. f(x) = 1/(1 + x)")
        print("4. f(x) = 2cos(x)")
        print("5. f(x) = sin(x^2)")
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
            chosen_function = "f(x) = 1/(1 + x)"
            is_function_chosen = True
        elif case == '4':
            function = f.func4
            chosen_function = "2cos(x)"
            is_function_chosen = True
        elif case == '5':
            function = f.func5
            chosen_function = "sin(x^2)"
            is_function_chosen = True
    if choice == "2" and is_function_chosen:
        a = float(input("Podaj lewą granicę całkowania a:"))
        b = float(input("Podaj prawą granicę całkowania b:"))
        eps = float(input("Podaj błąd:"))
        number = 2
        iteration = 1
        integral = 0
        while True:
            new_integral = simp.simpson(function, simp.get_arguments(a, b, number))
            if iteration > 1 and abs(new_integral - integral) < eps:
                break
            integral = new_integral
            iteration += 1
            number *= 2
        print("Wynik:", new_integral, ", liczba iteracji:", iteration)
    if choice == "3" and is_function_chosen:
        a = float(input("Podaj lewą granicę całkowania a:"))
        b = float(input("Podaj prawą granicę całkowania b:"))
        n = int(input("Podaj ilość węzłów (od 2 do 5):"))
        integral = leg.legendre(n, a, b, function)
        print("Wynik:", integral)
    if choice == "4":
        break
