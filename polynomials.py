def horner(x, polynomial_coeffs):
    polynomial_value = 0
    for coefficient in polynomial_coeffs:
        polynomial_value = polynomial_value * x + coefficient
    return polynomial_value


def horner_differential(x, polynomial_coeffs):
    differential_value = 0
    max_power = len(polynomial_coeffs) - 1
    for coefficient in polynomial_coeffs[:-1]:
        differential_value = differential_value * x + (coefficient * max_power)
        max_power -= 1
    return differential_value


def print_polynomial(polynomial_coeffs):
    polynomial_string = ""
    i = 0
    max_power = len(polynomial_coeffs) - 1
    for coefficient in polynomial_coeffs:
        if coefficient != 0 and max_power > 0:
            if i == 0:
                if coefficient == 1:
                    polynomial_string += f"x"
                elif coefficient == -1:
                    polynomial_string += f"-x"
                else:
                    polynomial_string += f"{coefficient}x"
            else:
                if coefficient > 0:
                    if coefficient == 1:
                        polynomial_string += f"+x"
                    else:
                        polynomial_string += f"+{coefficient}x"
                else:
                    if coefficient == -1:
                        polynomial_string += f"-x"
                    else:
                        polynomial_string += f"{coefficient}x"
            if max_power > 1:
                polynomial_string += f"^{max_power}"
        else:
            if max_power == 0:
                if coefficient > 0:
                    polynomial_string += f"+{coefficient}"
                else:
                    polynomial_string += f"{coefficient}"
        max_power -= 1
    return polynomial_string
