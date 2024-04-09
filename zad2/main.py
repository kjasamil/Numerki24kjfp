import file_handler as fh
import gauss as g
import os

while True:
    print("1. Rozwiąż wszystkie układy równań z danego folderu")
    print("2. Rozwiąż układ równań z pliku")
    print("3. Wyjście")
    case = input("Wybór: ")
    if case == '1':
        directory = input("Podaj ścieżkę do folderu: ")
        if os.path.exists(directory):
            for file in os.listdir(directory):
                print(file)
                AB = fh.read_equation_system(directory+str(file))
                print("Układ równań:")
                for row in AB:
                    print(row)
                print("Rozwiązanie: ", g.solve(AB))
                print("")
        else:
            print("Nie ma takiego folderu!")
    if case == '2':
        filename = input("Podaj ścieżkę do pliku: ")
        if os.path.exists(filename):
            AB = fh.read_equation_system(filename)
            print("Układ równań:")
            for row in AB:
                print(row)
            print("Rozwiązanie: ", g.solve(AB))
            print("")
        else:
            print("Nie ma takiego pliku!")
    if case == '3':
        break
