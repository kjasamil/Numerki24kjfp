import numpy as np

EPS = 10e-15


def solve(AB):
    n = len(AB[0]) - 1
    m = len(AB)
    if n != m:
        return "Nieodpowiednia liczba niewiadomych i równań"
    solution = [0.0 for _ in range(n)]
    for i in range(n - 1):  # i -> numer równania, które odejmujemy od pozostałych
        swap = False
        if abs(AB[i][i]) < EPS:  # jeżeli współczynnik < 10e-15 to wtedy python odczytuje to jako
            for k in range(i + 1, n):  # swap wierszy
                if abs(AB[k][i]) > EPS:
                    temp = AB[i]
                    AB[i] = AB[k]
                    AB[k] = temp
                    swap = True
                    break
            if not swap:
                return "Nie jest możliwe rozwiązanie tego układu równań."
        for j in range(i + 1, n):  # j -> numer równania, od którego odejmujemy równanie o numerze i
            # wyznaczamy mnożnik, przez który pomnożone zostanie równanie o numerze i oraz dodane do równania o nr j
            mul = -AB[j][i] / AB[i][i]
            for k in range(i, n + 1):
                AB[j][k] += mul * AB[i][k]

    if abs(AB[-1][-2]) < EPS < abs(AB[-1][-1]):  # sprawdzenie sprzeczności np 0 == 1
        return "sprzeczny"

    if abs(AB[-1][-2]) < EPS and abs(AB[-1][-1]) < EPS:
        return "nieoznaczony"

    for i in reversed(range(n)):
        b = AB[i][-1]
        for j in reversed(range(i + 1, n)):
            b -= AB[i][j] * solution[j]
        solution[i] = b / AB[i][i]

    return np.round(np.array(solution), 2)
