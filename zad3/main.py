import newton_interpolation as ni
import file_handler as fh
import functions as f
import os
from matplotlib import pyplot as plt
import numpy as np

NODES = []
ARGUMENTS = []
QUOTIENTS = []
is_function_chosen = False
nodes_mode = False
args_mode = False
chosen_function = ""
while True:
    if is_function_chosen:
        print("Wybrana funkcja:", chosen_function)
    if nodes_mode:
        print("Wybrano interpolację na węzłach ze wskazanego pliku.")
    print("1. Wybierz funkcję")
    print("2. Wczytaj węzły interpolacji z pliku")
    print("3. Wczytaj współrzędne x-owe węzłów interpolacji z pliku")
    print("4. Interpolacja")
    print("5. Koniec")
    case = input("Wybierz opcję: ")
    if case == '1':
        print("1. f(x) = |x - 2|")
        print("2. f(x) = x^3 + 2x^2 + x")
        print("3. f(x) = 2cos(x) + sin(x)")
        print("4. f(x) = |sin(x^2) + cos(x)|")
        case = input("Wybierz funkcję: ")
        if case == '1':
            function = f.func1
            chosen_function = "f(x) = |x - 2|"
            is_function_chosen = True
        elif case == '2':
            function = f.func2
            chosen_function = "f(x) = x^3 + 2x^2 + x"
            is_function_chosen = True
        elif case == '3':
            function = f.func3
            chosen_function = "2cos(x) + sin(x)"
            is_function_chosen = True
        elif case == '4':
            function = f.func4
            chosen_function = "|sin(x^2) + cos(x)|"
            is_function_chosen = True
    if case == '2':
        path = input("Podaj ścieżkę do pliku: ")
        if os.path.exists(path):
            NODES = fh.read_nodes(path)
            nodes_mode = True
            args_mode = False
            is_function_chosen = False
        else:
            print("Plik o takiej ścieżce nie istnieje!")
    if case == '3':
        path = input("Podaj ścieżkę do pliku: ")
        if os.path.exists(path):
            ARGUMENTS = fh.read_arguments(path)
            nodes_mode = False
            args_mode = True
        else:
            print("Plik o takiej ścieżce nie istnieje!")
    if case == '4':
        if nodes_mode:
            plt.grid(True)
            lin = np.linspace(NODES[0][0] - 5, NODES[0][-1] + 5, 1000)
            QUOTIENTS = ni.difference_quotients_val(NODES)
            plt.plot(lin, ni.newton_interpolation_val(lin, NODES, QUOTIENTS))
            # do dokończenia od tego momentu
