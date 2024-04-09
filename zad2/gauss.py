import numpy as np

EPS = 10e-15  # EPS = dokładność porównywania z zerem (w programie minimalny eps = 10^-15)


def solve(AB):
    n = len(AB[0]) - 1  # n = ilość niewiadomych
    m = len(AB)  # m = ilość równań
    if n != m:
        return "Nieodpowiednia liczba niewiadomych i równań"
    solution = [0.0 for _ in range(n)]
    for i in range(n - 1):  # i = numer równania, które będzie odjęte od pozostałych z odpowiednim mnożnikiem
        swap = False        # wybierane będą równania bez ostatniego
        if abs(AB[i][i]) < EPS:  # porównanie z zerem, sprawdzenie, czy trzeba znaleźć inny element podstawowy
            for k in range(i + 1, n):  # jeżeli trzeba, to szukamy w obecnej kolumnie elementu podstawowego
                if abs(AB[k][i]) > EPS:  # spośród pozostałych wierszy w macierzy
                    temp = AB[i]         # i podmieniamy obecny wiersz z wierszem, w którym ten element znaleźliśmy
                    AB[i] = AB[k]
                    AB[k] = temp
                    swap = True
                    break
            if not swap:  # m. el. Gaussa nie znajdzie rozwiązania, jeżeli nie udało się znaleźć elementu podstawowego
                return "Nie jest możliwe rozwiązanie tego układu równań."   # w danej kolumnie
        for j in range(i + 1, n):  # j = numer równania, od którego odejmujemy równanie o numerze i
            # wyznaczamy mnożnik, przez który pomnożone zostanie równanie o numerze i oraz dodane do równania o nr j
            mul = -AB[j][i] / AB[i][i]
            for k in range(i, n + 1):  # od pierwszej niezerowej wartości do ostatniej w wierszu (do wyrazu wolnego)
                AB[j][k] += mul * AB[i][k]  # zaktualizowanie wartości w wierszu j

    if abs(AB[-1][-2]) < EPS < abs(AB[-1][-1]):  # sprawdzamy, czy w ostatnim wierszu nie mamy sytuacji np. 0 == 1
        return "sprzeczny"                       # jeżeli do takiej sytuacji doszło, mamy układ sprzeczny

    if abs(AB[-1][-2]) < EPS and abs(AB[-1][-1]) < EPS:  # sprawdzamy, czy w ostatnim wierszu nie mamy sytuacji np.
        return "nieoznaczony"                            # 0 == 0, jeżeli tak, mamy układ nieoznaczony

    for i in reversed(range(n)):    # metodą podstawiania w tył znajdujemy kolejne rozwiązania
        b = AB[i][-1]               # b = wyraz wolny w danym wierszu
        for j in reversed(range(i + 1, n)):
            b -= AB[i][j] * solution[j]
        solution[i] = b / AB[i][i]  # solution[i] = i-te rozwiązanie

    return np.round(np.array(solution), 2)  # zaokrąglamy wynik
