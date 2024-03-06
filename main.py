import polynomials as p
import bisection as b


POLYNOMIAL = [1, -2**0.5, -1, -3]

print("Witaj!")
print("Aktualnie wybrana funkcja:")
print("Wielomian: ")
print(p.print_polynomial(POLYNOMIAL))
print(b.bisection_eps(2, 4, 0.0000001, POLYNOMIAL))
print(b.bisection_eps(-1, 1, 0.0000001, POLYNOMIAL))
print(b.bisection_iter(2, 4, 5, POLYNOMIAL))
print(b.bisection_iter(2, 4, 10, POLYNOMIAL))
print(p.horner_differential(0.47, POLYNOMIAL))
