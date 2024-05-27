def horner(x, polynomial_coeffs):
    polynomial_value = 0
    for coefficient in polynomial_coeffs:
        polynomial_value = polynomial_value * x + coefficient
    return polynomial_value
