import numpy as np

EPS = 10e-15


def solve(equation_system):
    unknowns_q = len(equation_system[0])
    equation_q = len(equation_system)
    solution = [0.0 for _ in range(unknowns_q - 1)]

    for i in range(equation_q - 1):  # i -> numer równania, które odejmujemy od pozostałych
        if abs(equation_system[i][i]) < EPS:  # jeżeli współczynnik < 10e-15 to wtedy python odczytuje to jako
            for k in range(i + 1, unknowns_q - 1):  # swap wierszy
                if abs(equation_system[k][i]) > EPS:
                    temp = equation_system[i]
                    equation_system[i] = equation_system[k]
                    equation_system[k] = temp
                    break

        for j in range(i + 1, equation_q):  # j -> numer równania, od którego odejmujemy równanie o numerze i
            # wyznaczamy mnożnik, przez który pomnożone zostanie równanie o numerze i oraz dodane do równania o nr j
            mul = -equation_system[j][i] / equation_system[i][i]
            for k in range(i, unknowns_q):  # k -> numer niewiadomej
                equation_system[j][k] += mul * equation_system[i][k]

    if abs(equation_system[-1][-2]) < EPS < abs(equation_system[-1][-1]):  # sprawdzenie sprzeczności np 0 == 1
        return "sprzeczny"

    for i in reversed(range(equation_q)):
        if abs(equation_system[i][i]) < EPS:  # sprawdzenie czy 0 == 0 czyli dużo rozwiązań
            return "nieoznaczony"

        b = equation_system[i][-1]
        for j in reversed(range(i + 1, equation_q)):
            b -= equation_system[i][j] * solution[j]
        solution[i] = b / equation_system[i][i]

    return np.round(np.array(solution), 2)
