import math


# laguerre zwraca tablicę współczynników wielomianu k-tego
# w kolejności od x z najwyższą potęgą do wyrazu wolnego żeby horner mógł obliczyć poprawnie
# wartość wielomianu
# wzór na współczynniki wzięty z neta (wolphram alpha chyba), nie patrz na wykład bo jest źle
# wzór podany na wykładzie nie pokrywa się z podanymi tam wielomianami

def laguerre(k):
    coefficients = []
    for m in range(k+1):
        coefficients.append(((-1)**m * math.comb(k, m)) / math.factorial(m))
    return coefficients[::-1]
