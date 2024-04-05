EPS = 10e-15


def solve(equation_system):
    unknowns_q = len(equation_system[0])
    equation_q = len(equation_system)
    solution = []
    for i in range(0, unknowns_q - 1):
        solution.append(0.0)
    for i in range(0, equation_q - 1):  # i -> numer równania, które odejmujemy od pozostałych
        for j in range(i + 1, equation_q):  # j -> numer równania, od którego odejmujemy równanie o numerze i
            if abs(equation_system[i][i]) < EPS:  # jeżeli współczynnik < 10e-15 to wtedy python odczytuje to jako
                return "problem xd"                      # 0 i doszłoby do dzielenia przez 0, czego nie chcemy
            # wyznaczamy mnożnik, przez który pomnożone zostanie równanie o numerze i oraz dodane do równania o nr j
            mul = -equation_system[j][i] / equation_system[i][i]
            for k in range(i, unknowns_q):  # k -> numer niewiadomej
                equation_system[j][k] += mul * equation_system[i][k]
    if equation_system[-1][-2] == 0 and equation_system[-1][-1] != 0:
        return "sprzeczny"
    for i in reversed(range(0, equation_q)):
        b = equation_system[i][-1]
        for j in reversed(range(i + 1, equation_q)):
            b -= equation_system[i][j] * solution[j]
        if abs(equation_system[i][i]) < EPS:
            return "nieoznaczony"
        solution[i] = b / equation_system[i][i]
    return solution
