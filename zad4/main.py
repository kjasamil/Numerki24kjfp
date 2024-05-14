import functions as f
import legendre as leg

while True:
    print("1. f(x) = 2x + 2")
    print("2. f(x) = |x - 2|")
    print("3. f(x) = x^2 + 2")
    print("4. f(x) = 2cos(x) + sin(x)")
    print("5. f(x) = |sin(x^2) + cos(x)|")
    function = None
    while function is None:
        case = input("Wybierz funkcję: ")
        if case == '1':
            function = f.func1
            chosen_function = "f(x) = 2x + 2"
        if case == '2':
            function = f.func2
            chosen_function = "f(x) = |x - 2|"
        elif case == '3':
            function = f.func3
            chosen_function = "f(x) = x^2 + 2"
        elif case == '4':
            function = f.func4
            chosen_function = "2cos(x) + sin(x)"
        elif case == '5':
            function = f.func5
            chosen_function = "|sin(x^2) + cos(x)|"

    knots = int(input("Podaj liczbę węzłów od 2 do 5: "))
    a = 0
    b = 0
    while b <= a:
        a = float(input("Podaj początek przedziału: "))
        b = float(input("Podaj koniec przedziału: "))
    print(leg.legendre(knots, a, b, function))
